# GPT-6.1 Terra + Sol Codex 模型路由器：节省令牌，选对模型和推理强度

[英文说明](README.md) | **中文说明**

[![许可证：MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![最新版本](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

模型路由器会在任务开始前推荐模型和推理强度。你自己选好推荐组合，再输入「执行」继续。它不会暗中切换模型，不改速度设置，也不保证固定的令牌节省比例。

## 1.3.0 新增 GPT-6.1 Terra

现在支持 **GPT-6 Luna、GPT-6.1 Terra、GPT-6.1 Sol 和 GPT-6 Astra**。

Terra 用于有明确资料和验收标准的写作、图表与界面解读、目标明确的软件操作，以及原因已知、范围有限且可以回归检查的代码修复。复杂项目仍用 Sol；不能因为第一步是看截图，就把整个复杂任务交给 Terra。

依据：[Terra 官方规格](https://developers.openai.com/api/docs/models/gpt-6.1-terra)、[官方模型选择说明](https://learn.chatgpt.com/docs/model-selection)，核对日期为 2026 年 10 月 28 日。

仓库地址和技能名称保持不变，避免旧安装找不到更新。**1.3.0 是工具版本，GPT-6.1 是模型系列。**

## 第一步：安装

### 最方便：让 Codex 帮你安装

只选一个档位，复制对应的整段话发送给 Codex。单独发送仓库网址，不等于要求安装。

**20 美金档**

```text
请使用技能安装器从 GitHub 仓库 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.3.0，路径使用 profiles/20-usd，名称使用 model-router-20。运行已安装技能的全局路由脚本，再用本机已有的运行环境运行 scripts/router-update.py enable-hooks，配置更新提醒。保留我的其他 AGENTS.md 规则及检查脚本。告诉我如何审核并信任新配置，不要绕过审核；缺少运行环境时先问我，不要擅自安装。分别说明哪些步骤已验证。
```

**高额度档，例如五倍或二十倍额度**

```text
请使用技能安装器从 GitHub 仓库 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.3.0，路径使用 .，名称使用 model-router。运行已安装技能的全局路由脚本，再用本机已有的运行环境运行 scripts/router-update.py enable-hooks，配置更新提醒。保留我的其他 AGENTS.md 规则及检查脚本。告诉我如何审核并信任新配置，不要绕过审核；缺少运行环境时先问我，不要擅自安装。分别说明哪些步骤已验证。
```

这里的档位是本项目的额度使用策略，不是官方订阅名称，也不是额度保证。两个档位使用同一套四模型规则；20 美金档在基础判断完成后，额外转换一次：

| 原本的 Astra 推荐 | 20 美金档最终推荐 |
| --- | --- |
| Astra 轻或中 | GPT-6.1 Sol 极高 |
| Astra 高、极高、最大或超强 | GPT-6 Astra 轻 |

Luna、Terra 和 Sol 的基础推荐不变。转换后的 Astra 轻不会再转一次，也不会把 Astra 直接映射到 Terra。这是额度偏好，不代表能力相等。高额度档保留原始推荐。

### 手动下载安装

下载 [1.3.0 压缩包](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.3.0.zip)。20 美金档把 `profiles/20-usd` 复制到 `<CODEX_HOME>/skills/model-router-20`；高额度档把根目录技能文件复制到 `<CODEX_HOME>/skills/model-router`。

`SKILL.md`、`GLOBAL-ROUTING.md`、`version.json`、`agents/`、`references/` 和 `scripts/` 必须放在一起。已有安装先备份到技能目录以外；只保留一个档位。

默认配置目录：Windows 为 `%USERPROFILE%\.codex`，其他系统为 `~/.codex`。在安装好的技能目录运行：

**Windows 命令**

```powershell
.\scripts\global-routing.ps1
python .\scripts\router-update.py enable-hooks
```

**其他系统命令**

```sh
sh ./scripts/global-routing.sh
python3 ./scripts/router-update.py enable-hooks
```

需要可运行的 Python 3.10 或更高版本；必要时把程序名换成完整路径。第一条命令只更新用户级 `AGENTS.md` 的受管理区块，保留其他规则并备份。第二条命令添加更新提醒，保留其他检查脚本。

首次配置后，请在客户端支持的脚本审核入口检查并信任新配置；命令行客户端使用 `/hooks`。必要时新建会话或重启。**写入配置成功，不等于客户端已经运行成功。** 客户端、运行环境或信任条件不满足时，普通路由仍可使用，只是没有自动提醒。[官方脚本说明](https://learn.chatgpt.com/docs/hooks)

Terra 需要 Codex 命令行版本 **0.159.0 或更高**。实际可用性仍取决于账号、客户端、工作区及发布进度；推荐模型不存在时应说明差异，不可偷偷替换。[官方模型可用性](https://learn.chatgpt.com/docs/models)

## 第二步：使用

安装并完成全局设置后，**每次像平时一样直接输入任务，不需要在每句话或每个新对话前加前缀。** 不是第一次写一次前缀就永久启用，真正起作用的是上面的全局设置。

1. 输入你的任务。
2. 查看模型和推理强度建议。
3. 在 Codex 里选好推荐组合。
4. 单独发送「执行」，继续刚才的任务。

普通推荐只有三行，例如：

```text
模型：GPT-6.1 Terra；推理强度：中
原因：已有明确资料和核对标准，适合范围有限的写作任务。
操作：在模型选择器中选择模型和推理强度，然后发送“执行”。
```

只有想强制“只推荐、不执行”时，才显式使用与你的档位对应的 `$model-router-20` 或 `$model-router`。继续处理复杂问题时，会按未完成的完整任务判断，不应因上一项任务用了 Luna 或 Terra 就一直沿用。

## 什么时候推荐哪个模型？

| 任务 | 基础模型 | 常用推理起点 |
| --- | --- | --- |
| 按明确规则提取、整理表格或替换指定文字与样式 | GPT-6 Luna | 轻或中 |
| 按给定事实写作、解读图表与界面、明确的软件操作、可回归检查的小范围已知修复 | GPT-6.1 Terra | 中；判断很少时用轻 |
| 细节密集、但仍有明确边界的图表或视觉解读 | GPT-6.1 Terra | 高 |
| 不满足 Terra 边界的日常开发、资料整合与分析 | GPT-6.1 Sol | 中 |
| 功能联动、未知或反复失败的缺陷、状态或权限变化 | GPT-6.1 Sol | 高 |
| 单一领域特别困难的问题 | GPT-6.1 Sol | 极高 |
| 满足条件的困难整合、长链条依赖或隐蔽错误代价高的任务 | GPT-6 Astra | 轻或中；高风险或难验证时用高 |

这些起点是本项目的路由策略，不是官方能力等价表。Terra 不负责需求不清、状态和数据联动、反复失败或隐蔽错误代价高的复杂项目；不能仅靠把推理调到最大，就把不合适的任务留在 Terra。

Luna 仍要求单一、规则明确、不需要调查或设计、容易直接核对。Astra 需要至少两个真实复杂信号，同时存在协调困难、长上下文依赖或隐蔽错误风险；普通交付或多文件本身不够。20 美金档只在基础判断之后转换一次。

本次核对的本机目录列出了四个模型的轻至最大档，Terra、Sol 和 Astra 另有超强档；以用户实际选择器为准。Terra 的接口支持无推理，但本机 Codex 目录没有这个选项，**不能把接口参数当成客户端可选项**。超强属于客户端能力，可用不等于允许委派任务。速度设置不动。

## 已安装用户怎么更新？

使用 1.2.1 或更新版本时，单独发送「检查路由器更新」可立即检查；单独发送「更新路由器」才会升级同一档位，不会执行正在等待确认的任务。

旧版、更新器不可用或需要手动重新安装时，发送：

```text
请把我已安装的 Codex 模型路由器更新到 alanliuc-a11y/codex-model-router-gpt-6-1 的 v1.3.0。保留当前档位：model-router-20 使用 profiles/20-usd，model-router 使用根目录。先把旧技能及 AGENTS.md、hooks.json 备份到技能目录外，再使用技能安装器安装同一档位，因为安装器不会覆盖旧目录。运行全局路由脚本并核对版本清单及文件校验值。保留其他规则和检查脚本，只保留一个生效档位。保留更新提醒原来的开关状态；原本启用或我明确要求时，才运行 scripts/router-update.py enable-hooks。说明必要的信任审核，不要绕过审核。安装或配置失败时恢复旧目录及配置。
```

确认有新版时，推荐下方最多增加第四行：

> 更新：模型路由器已有新版（版本号），输入“更新路由器”即可更新。

前台只读缓存，后台每二十四小时最多检查一次，失败也会缓存；手动检查可立即刷新。匿名接口限流时使用官方最新发布链接，不读取凭据。首次提醒可能出现在下一项任务；检查不可用不能说“已经是最新版”。

只有创建新的 GitHub 正式发布版本才会触发提醒，仅提交代码不会触发。检查不发送任务、聊天或密钥，但联网会透露通常的网络信息。更新会校验下载、备份完整旧技能及配置，安装中可捕获的失败会恢复旧版；备份保留，关闭的提醒不会被擅自重新打开。文件校验不是独立于仓库的安全签名。

这不是系统推送，也不是点击链接就能安装。修改过技能文件或使用 Git 克隆安装的用户应手动升级；突然退出或恢复时写入失败可能需要人工处理。见[测试与恢复步骤](docs/update-testing.zh-CN.md)。

关闭提醒：`python scripts/router-update.py disable-hooks`。关闭路由需另外使用全局脚本的 `-Disable` 或 `--disable`；预览使用 `-Preview` 或 `--preview`。完整卸载前分别关闭两者。

## 真实操作截图

以下为旧版截图，仅展示“先切换、再确认”的步骤，不代表当前模型推荐；没有把旧截图改名冒充 Terra 截图。

![旧版 Luna 示例](docs/screenshots/zh-00-luna-light-example.png)
![第一步：在选择器切换模型与推理强度](docs/screenshots/zh-01-switch-sol-high.png)
![第二步：输入执行继续任务](docs/screenshots/zh-02-confirm-execute.png)
![旧版 Astra 确认流程](docs/screenshots/zh-03-astra-confirm-execute.png)

## 能节省百分之六十的令牌吗？

不能保证固定比例。请用同样的输入和推理强度比较有代表性的任务，再单独调整推理强度，记录正确性、总用量、得到可用结果的时间及返工。较小模型仍达到质量要求，才算真正提高效率。

接口价格不等于 Codex 订阅额度消耗。旧 GPT-6 Sol 榜单成绩不能算作 GPT-6.1 Terra 或 Sol 成绩，本次不编写可直接比较的榜单档位排名。[官方比较方法](https://learn.chatgpt.com/docs/model-selection)

## 仓库内容与贡献

- `SKILL.md`、`GLOBAL-ROUTING.md`、`agents/openai.yaml`：技能规则、全局兜底及展示信息。
- `profiles/20-usd/`：可独立安装的 20 美金档。
- `scripts/router-update.py`、`version.json`、`references/updating.md`：更新提醒、校验及安全升级。
- `scripts/build-manifests.py`、`tests/test_updates.py`：打包与离线测试。
- [路由验收案例](docs/routing-cases.md)、[更新测试](docs/update-testing.zh-CN.md)、[更新记录](CHANGELOG.md)、[贡献说明](CONTRIBUTING.md)。

离线测试运行 `python -m unittest discover -s tests -v`。技能创建工具的 `quick_validate.py <技能目录>` 检查结构，不证明每次模型推荐都最优；重要任务仍需实际验收。代码及技能采用 [MIT 许可证](LICENSE)。

搜索关键词：节省令牌、节省 Codex 令牌、节省 token、降低 Codex 消耗、模型路由、GPT-6.1 Terra、GPT-6.1 Sol、GPT-6 Astra、GPT-6 Luna、推理强度、技能更新提醒。
