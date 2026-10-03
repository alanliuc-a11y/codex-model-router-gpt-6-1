# GPT-6.1 Sol Codex 模型路由器：节省令牌，选对模型和推理强度

[英文说明](README.md) | **中文说明**

[![许可证：MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![Codex 技能](https://img.shields.io/badge/Codex-skill-22c55e.svg)](SKILL.md) [![最新版本](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

**模型路由器**是一个小型 Codex 技能。它会在你开始任务**之前**，从 GPT-6 Luna、GPT-6.1 Sol 和 GPT-6 Astra 中建议一个足够胜任的模型，并单独推荐推理强度；当任务需要跨多个环节完成端到端整合时，会使用 GPT-6 Astra。目标很直接：在质量够用的前提下，避免为不需要的模型能力或推理消耗付费。

如果你想节省令牌、节省 Codex 令牌、降低 Codex 令牌消耗，或提高 Codex 的使用效率，这个技能会在执行前给出一个可操作的选择建议。

## 2026 年 10 月 4 日更新：支持 GPT-6.1 Sol

| 任务 | 默认模型 | 建议起点 |
| --- | --- | --- |
| 明确、单一、容易核对的整理或修改 | GPT-6 Luna | 轻或中 |
| 日常开发、文档、已知问题修复 | GPT-6.1 Sol | 中 |
| 多功能联动、调查原因、反复失败的问题 | GPT-6.1 Sol | 高 |
| 单一领域特别困难的问题 | GPT-6.1 Sol | 极高 |
| 满足后文条件的跨系统完整任务 | GPT-6 Astra | 轻或中；隐蔽错误代价高时用高 |

20 美金档现在把原本的 Astra 轻或中映射为 **GPT-6.1 Sol 极高**；原本的 Astra 高及以上仍映射为 Astra 轻，只转换一次。这是额度使用偏好，不代表能力相等或已测得节省多少额度。

官方把 GPT-6.1 Sol 定位为适合复杂编程、计算机操作和专业任务的模型，成本低于 Astra。我们据此把日常默认模型升级为 6.1；升级时先保留推理强度，再用实际任务比较是否可以降低。[官方模型资料](https://developers.openai.com/api/docs/models/gpt-6.1-sol)

AutomationBench 可辅助比较跨应用任务，但旧版 GPT-6 Sol 的成绩不能算作 6.1 的成绩。本次未核实到可直接比较的 6.1 推理档位成绩，因此不编写分数或保证节省比例。[官方榜单](https://zapier.com/benchmarks)

目标明确、检查充分的跨系统任务可以先用 GPT-6.1 Sol 高；跨多个环节且协调困难、长上下文依赖多或隐蔽错误代价高的任务，再评估 Astra。多文件或普通交付步骤本身不够构成升级依据。

本机核对到三个模型均有轻至最大档，Sol 和 Astra 另有超强档；实际推荐仍以用户模型选择器为准。GPT-5.6 系列仅保留为用户明确选择的旧版选项，没有已核实的 GPT-6 Terra。

下方截图是旧版本操作记录，部分仍显示 GPT-5.6；仅说明切换和确认步骤，新任务请以上表为准。

## 已安装用户怎么升级

在 Codex 中复制发送：

```text
请把我已安装的 Codex 模型路由器更新到 alanliuc-a11y/codex-model-router-gpt-6-1 仓库的 v1.1.0 版本。先检测当前安装档位：model-router-20 使用 profiles/20-usd，model-router 使用仓库根目录。技能安装器不会覆盖已有目录，请先把旧技能备份到技能目录外，再使用技能安装器安装同一档位，运行全局启用脚本，保留其他 AGENTS.md 规则并核对安装文件。只保留一个生效的路由器；如果安装失败，请恢复备份。
```

技能名称保持不变。GPT-6.1 是支持的模型版本，v1.1.0 是本工具的发布版本。旧仓库地址会重定向，今后的安装请使用新地址。

## 先选择安装档位

请按 Codex 可用额度选择一个档位。这里的名称只是路由策略，不是 OpenAI 官方订阅名称，也不代表保证的额度。

| 你的可用额度 | 安装档位 | Astra 的处理方式 |
| --- | --- | --- |
| 20 美金档 | **20 美金档** | 原本会推荐 Astra 轻或中的任务，改为 Sol + 极高；原本会推荐 Astra 高、极高、最大或超强的任务，改为 Astra + 轻。 |
| 高于 20 美金档，例如 5× 或 20× | **高额度档** | 沿用本仓库现有的完整路由逻辑。 |

一次只安装一个档位。两个档位都会管理用户级 `AGENTS.md` 中同一个区块；之后运行另一个档位的启用脚本，会替换当前生效的全局路由规则。

## 最方便的安装方式：直接让 Codex 安装

### 20 美金档

在 Codex 中复制并发送下面整段话：

```text
请使用技能安装器从 GitHub 仓库 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.1.0 版本的 Codex 技能；仓库内路径使用 profiles/20-usd，技能名称使用 model-router-20。安装完成后，请运行当前操作系统对应的附带脚本，启用它的全局路由功能；保留我现有的 AGENTS.md 规则，并在准备好后告诉我。
```

### 高额度档

在 Codex 中复制并发送下面**整段话**。不要只发送一个裸 GitHub 链接。

```text
请使用技能安装器从 GitHub 仓库 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.1.0 版本的 Codex 技能；仓库内路径使用 .，技能名称使用 model-router。安装完成后，请运行当前操作系统对应的附带脚本，启用它的全局路由功能；保留我现有的 AGENTS.md 规则，并在准备好后告诉我。
```

高额度档位于仓库根目录，因此路径是 `.`；20 美金档位于 `profiles/20-usd`。全局路由启用完成后，以后的任务都可以像平时一样直接输入，不需要每次添加 skill 前缀。

## 手动下载安装

下载 [v1.1.0 压缩包](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.1.0.zip) 并解压。20 美金档把 `profiles/20-usd` 内的文件复制到用户技能目录中的 `model-router-20` 文件夹；高额度档把根目录技能文件复制到 `model-router` 文件夹。`SKILL.md`、`GLOBAL-ROUTING.md`、`agents` 和 `scripts` 必须放在一起。已有安装先备份，然后运行下方全局启用命令。

默认用户技能目录：Windows 为 `%USERPROFILE%\.codex\skills`，其他系统为 `~/.codex/skills`。

## 第一步：安装

高额度档请把本仓库克隆到 Codex skills 目录中，文件夹名称使用 `model-router`：

```text
<CODEX_HOME>/skills/model-router/
├── SKILL.md
└── agents/openai.yaml
```

20 美金档请将 `profiles/20-usd` 安装为 `model-router-20`。重启 Codex 或新建一个任务，让应用重新发现所选 skill；然后在该 skill 目录中运行一次全局启用命令：

**Windows PowerShell**

```powershell
.\scripts\global-routing.ps1
```

**macOS / Linux**

```sh
./scripts/global-routing.sh
```

这一次命令就是全局设置。请注意：这**不是**在聊天里第一次加一次 `$model-router` 就永久生效；前缀本身不是开关。脚本只会添加或更新用户级 `AGENTS.md` 中带标记的 Model Router 区块：保留原有规则，并在修改前创建备份。PowerShell 使用 `-Preview`、macOS/Linux 使用 `--preview` 可先预览；分别用 `-Disable`、`--disable` 删除受管理的区块。

## 第二步：使用

完成第一步后，每次对话都像平时一样直接输入任务即可。**不需要**在每次对话前添加 skill 前缀。Codex 应先给出模型和推理强度建议，再开始工作。

只有在希望强制进入“只推荐、不执行”时，才显式添加与你所选档位对应的 `$model-router` 或 `$model-router-20` 作为兜底，例如：

```text
$model-router 审核这份数据库迁移方案，推荐足够且最节省的模型和推理强度；不要执行审核。
```

技能会返回模型、推理强度和简短原因。请先在 Codex 中选好对应组合，再开始实际任务。中文交流时，确认词为 `执行` 或 `按推荐执行`。

## 看一眼实际操作流程

以下是真实 Codex 截图，统一放在浅色教程卡片中。模型路由器不会替你暗中切换：先在右下角模型选择器中选好建议档位，再输入「执行」。

### 轻量、容易核验的任务

![轻量任务可从 GPT-6 Luna 和轻推理强度开始](docs/screenshots/zh-00-luna-light-example.png)

### 常规审阅：先切换，再确认

![第 1 步：路由器建议 GPT-6.1 Sol 和高推理强度，在模型选择器中按建议设置](docs/screenshots/zh-01-switch-sol-high.png)

![第 2 步：设置完成后输入执行，任务才会继续](docs/screenshots/zh-02-confirm-execute.png)

### 当端到端整合复杂度达到 Astra 的优势区间

![跨系统且难验证的任务被推荐到 GPT-6 Astra 和超强推理强度，确认后输入执行](docs/screenshots/zh-03-astra-confirm-execute.png)

这些截图展示的是“建议与确认”的流程，不是自动切换模型。可用模型和选择器标签会因账号与 Codex 发布版本而不同。

## 它为什么有用？

很多人会一直使用最强模型和最高推理强度。面对困难任务，这样做可能合理；但对一次明确的修改、规则固定的检查或可重复的转换来说，往往没有必要。

模型路由器会建议一个尽量低、但仍适合的起点：

- **GPT-6 Luna**：范围窄、可重复、结果容易验证的工作。
- **GPT-6.1 Sol**：日常开发和文档任务默认用中；多功能联动、原因不明的问题或需要深入判断时用高；特别困难时评估极高。
- **GPT-6 Astra**：需要跨多个高强度环节、系统、阶段或交付物完成端到端整合的任务。

它会把“模型”和“推理强度”分开建议，避免所有任务都默认使用最高推理强度。Astra 不会成为新的默认模型；只要 Luna 或 Sol 足以达到质量要求，路由器仍会优先选择成本更低的模型。

### 什么情况下才会推荐 Luna

只有目标单一、解决方式明确、不需要调查或处理多功能与状态联动，而且结果容易直接核验时，才推荐 Luna。多功能发布台、身份规则、上传同步、播放状态、跨页面修改、原因不明或反复失败的问题，都排除 Luna。每个新任务都会结合对话上下文重新判断，不能因为前面几轮是小改动，就一直沿用 Luna。两档都先执行这些判断，再应用额度策略。

可查看[路由核对案例](docs/routing-cases.md)，对照两档的预期差别。

### Astra 的判断条件

当任务同时满足以下至少两项时，路由器会推荐 Astra：

- 同时包含三种或以上高强度工作，例如编程、浏览、研究、电脑操作、数据分析、媒体制作或专业文档。
- 需要从调研、实现、验证一直负责到交付或发布。
- 涉及多个相互影响的系统、应用、仓库或交付物类型。
- 执行链很长，前面的小错误可能悄悄传递到后续阶段。
- 缺少可靠的端到端验证，存在冲突证据、外部影响代价高或故障难以发现。

现在不再要求先证明 Sol 会失败。两项信号应当体现真正的协调困难、长上下文依赖或隐蔽错误代价；目标明确且检查充分的跨系统流程可先用 GPT-6.1 Sol 高。单项高难度工作，或只在一个领域内进行深度分析，仍然会推荐 Sol 或更低档位。

## 它不会做什么

- 不会自动切换一个已经开始运行的任务的模型。
- 不会修改你的速度设置。
- 不会声称知道你当前 Codex 界面里选中了什么。
- 不会承诺“节省 60% Token”这类固定比例。

固定百分比并不可靠：实际节省取决于任务类型、原先使用的模型与推理强度、对话长度，以及你要求达到的质量标准。

## “效率提高”如何验证？

这个 skill 所说的效率是可检验的：当更小的模型或更低的推理强度仍能达到质量要求时，避免使用更大的配置。

建议选择一组有代表性的任务，把平时的设置与推荐设置进行对比，记录：

1. 任务是否完成，输出是否完整。
2. 总 Token 消耗与成本。
3. 得到可用结果所需的时间。
4. 是否出现返工、失败或必须升级配置的情况。

只有当质量检查也通过时，Token 更低才算真正的效率提升。OpenAI 的模型指南同样建议使用有代表性的任务比较，并尝试降低一档推理强度，而不是假定最高设置总是最佳取舍。[OpenAI 模型指南](https://developers.openai.com/api/docs/guides/latest-model)

## 重要说明

- 一个任务的根模型会在任务开始前确定。skill 只能建议，不能在任务运行中自动切换根模型。
- `标准` 不是推理强度建议；它可能是速度或执行模式。
- 在 Codex 中，本路由器只管理 GPT-6 Luna、GPT-6.1 Sol 和 GPT-6 Astra。若你同时安装了通用的跨平台模型路由器，应将后者设为仅显式调用；否则它的“当前可用模型中最低够用”策略可能与这里的受管模型目录冲突。
- 如果模型选择器中没有任何受管模型，路由器应报告这一不一致，而不是静默改用 GPT-5.4 Mini 等其他选项。
- OpenAI 的接口文档列出的 GPT-6 Astra 推理强度对应轻、中、高、极高和最大。超强以 Codex 实际提供的选项为准，不作为通用接口推理参数。
- 如果模型选择器缺少推荐的模型，应说明差异并确认可用选项，不应悄悄替换为旧版模型。
- 路由器是决策辅助工具，不是质量保证。若错误代价高或很难发现，应主动使用更强模型或更高推理强度。

官方资料：[GPT-6 Astra 模型页面](https://developers.openai.com/api/docs/models/gpt-6-astra)和[OpenAI 模型指南](https://developers.openai.com/api/docs/guides/latest-model)。

## 搜索关键词

节省 Token · 节省 Codex Token · 降低 Codex Token 消耗 · 提高 Codex 效率 · Codex 模型选择 · Codex 推理强度 · GPT-6 Luna · GPT-6.1 Sol · GPT-6 Astra · Astra 模型路由

## 仓库内容

- `SKILL.md`：由 Codex 加载的路由规则。
- `agents/openai.yaml`：skill 的展示信息与自动发现策略。
- `GLOBAL-ROUTING.md`：用于全局模式的小型、受管理用户级规则区块。
- `scripts/global-routing.ps1`、`scripts/global-routing.sh`：一次性启用、预览、更新和禁用命令。
- `profiles/20-usd/`：可独立安装的 20 美金档，含自己的 skill 信息和全局路由脚本。
- `README.md`、`README.zh-CN.md`：英文在前、中文配套的说明文档。
- `LICENSE`：允许复用和分发的 MIT 许可证。
- `CONTRIBUTING.md`：提交问题和贡献的安全指引。

## 版本与贡献

稳定版本请见 [Releases](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)；安装问题、路由案例、翻译修正和聚焦的 Pull Request，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 校验 skill

在安装了 Skill Creator 工具的环境中运行：

```text
python quick_validate.py <model-router 路径>
```

该校验会检查目录结构与 frontmatter；它不会证明每一次建议都最优。对重要工作，发布或采用前仍应使用有代表性的任务进行验证。
