#!/usr/bin/env sh
set -eu

disable=0
preview=0
codex_home="${CODEX_HOME:-$HOME/.codex}"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --disable) disable=1 ;;
    --preview) preview=1 ;;
    --codex-home)
      shift
      [ "$#" -gt 0 ] || { echo "--codex-home needs a value" >&2; exit 2; }
      codex_home="$1"
      ;;
    *) echo "Unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
skill_dir=$(dirname "$script_dir")
fragment_path="$skill_dir/GLOBAL-ROUTING.md"
agents_path="$codex_home/AGENTS.md"
start_marker='<!-- model-router:global-start -->'
end_marker='<!-- model-router:global-end -->'

[ -f "$fragment_path" ] || { echo "Missing routing fragment: $fragment_path" >&2; exit 1; }
existing=$( [ -f "$agents_path" ] && cat "$agents_path" || true )
has_start=$(printf '%s' "$existing" | grep -F -c "$start_marker" || true)
has_end=$(printf '%s' "$existing" | grep -F -c "$end_marker" || true)
[ "$has_start" = "$has_end" ] || { echo "Refusing to edit $agents_path because its Model Router markers are incomplete." >&2; exit 1; }

tmp_file=$(mktemp "${TMPDIR:-/tmp}/model-router-agents.XXXXXX")
trap 'rm -f "$tmp_file"' EXIT HUP INT TERM

if [ "$disable" -eq 1 ]; then
  if [ "$has_start" = "0" ]; then
    echo "Model Router global workflow is not enabled in $agents_path."
    exit 0
  fi
  awk -v start="$start_marker" -v end="$end_marker" '
    $0 == start { skipping=1; next }
    $0 == end { skipping=0; next }
    !skipping { print }
  ' "$agents_path" > "$tmp_file"
  action="remove the managed Model Router block from"
else
  if [ "$has_start" = "0" ]; then
    { [ -z "$existing" ] || printf '%s\n\n' "$existing"; cat "$fragment_path"; printf '\n'; } > "$tmp_file"
    action="add the managed Model Router block to"
  else
    awk -v start="$start_marker" -v end="$end_marker" -v fragment="$fragment_path" '
      $0 == start {
        while ((getline line < fragment) > 0) print line
        close(fragment)
        skipping=1
        next
      }
      $0 == end { skipping=0; next }
      !skipping { print }
    ' "$agents_path" > "$tmp_file"
    action="update the managed Model Router block in"
  fi
fi

if [ "$preview" -eq 1 ]; then
  echo "Would $action $agents_path"
  exit 0
fi

mkdir -p "$codex_home"
if [ -f "$agents_path" ]; then
  backup_path="$agents_path.model-router-backup-$(date -u +%Y%m%d%H%M%S)"
  cp "$agents_path" "$backup_path"
  echo "Backup: $backup_path"
fi
mv "$tmp_file" "$agents_path"
trap - EXIT HUP INT TERM
echo "Completed: $action $agents_path"
