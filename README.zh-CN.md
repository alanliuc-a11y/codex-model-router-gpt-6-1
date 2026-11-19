# Codex 模型路由器：支持 GPT-6.2，保留 GPT-6.1 Sol 的性价比选择

[英文说明](README.md) | **中文说明**

[![许可证：MIT](https://img.shields.io/badge/License-MIT-7c3aed.svg)](LICENSE) [![最新版本](https://img.shields.io/github/v/release/alanliuc-a11y/codex-model-router-gpt-6-1?display_name=tag&color=06b6d4)](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/releases)

任务开始前，先推荐够用的模型和推理强度。你自己选好组合，再输入「执行」继续。不会暗中换模型，不改速度，也不保证固定的令牌节省比例。

## 1.4.0：支持新版，但不为追新牺牲性价比

候选模型为 **GPT-6 Luna、GPT-6.1 Terra、GPT-6.1 Sol、GPT-6.2 Sol 和 GPT-6.2 Astra**。6.1 Sol 仍是正常的性价比候选，不再因为新版发布就被降为旧版兜底。

按质量、可用模型、上下文、推理消耗及返工综合选择。**ChatGPT Plus** 策略保留已经验证好用的 6.1 Sol 基线；**ChatGPT Pro** 可以先评估 6.2 Sol，但仍保留 6.1 的经验优势。这是项目策略，不是官方路由算法。

官方基准积分单价中，6.1 Sol 与 6.2 Sol 相同，不能直接说谁完成整个任务一定更便宜。官方还明确说明：6.1 Sol 的订阅用量没有长上下文附加费。订阅额度、额外积分和接口账单要分开判断。[官方计费资料](https://learn.chatgpt.com/docs/pricing)，核对日期为 2026 年 11 月 19 日。

## 第一步：按官方订阅名称安装

根据自己的实际订阅选择，不再用月费金额分档，也不从模型列表猜订阅。只安装一个策略。

### ChatGPT Plus

把下面整段话发送给 Codex：

```text
请使用技能安装器从 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.4.0，路径使用 profiles/20-usd，名称使用 model-router-20，采用 ChatGPT Plus 性价比优先策略。运行已安装技能的全局路由脚本，再用本机已有的运行环境运行 scripts/router-update.py enable-hooks。保留其他 AGENTS.md 规则及检查脚本，告诉我如何审核并信任新配置，不要绕过审核。缺少运行环境时先问我，并分别说明哪些步骤已验证。
```

### ChatGPT Pro

```text
请使用技能安装器从 alanliuc-a11y/codex-model-router-gpt-6-1 安装 v1.4.0，路径使用 .，名称使用 model-router，采用 ChatGPT Pro 策略。运行已安装技能的全局路由脚本，再用本机已有的运行环境运行 scripts/router-update.py enable-hooks。保留其他 AGENTS.md 规则及检查脚本，告诉我如何审核并信任新配置，不要绕过审核。缺少运行环境时先问我，并分别说明哪些步骤已验证。
```

其他订阅、工作区席位或接口密钥使用方式，应先核对真实的模型权限及用量限制，不能一律按 Pro 处理，也不能保证五个模型都可用。Pro 内部的额度也并不完全相同。

`model-router-20` 与 `profiles/20-usd` 仅保留为历史兼容标识，**不是给用户选择的订阅分档名称**。仓库网址里的 `gpt-6-1` 同样为兼容旧更新器保留，不限制支持的模型版本。

### 手动下载安装

下载 [1.4.0 压缩包](https://github.com/alanliuc-a11y/codex-model-router-gpt-6-1/archive/refs/tags/v1.4.0.zip)。Plus 使用 `profiles/20-usd`，安装到 `<CODEX_HOME>/skills/model-router-20`；Pro 使用根目录技能文件，安装到 `<CODEX_HOME>/skills/model-router`。

`SKILL.md`、`GLOBAL-ROUTING.md`、`version.json`、`agents/`、`references/` 和 `scripts/` 必须放在一起。已有安装先备份到技能目录外，只保留一个策略。

在已安装的技能目录运行：

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

需要可用的 Python 3.10 或更高版本，必要时使用程序完整路径。默认配置目录为 Windows 的 `%USERPROFILE%\.codex` 或其他系统的 `~/.codex`。配置保留其他规则及检查脚本，并备份改动。

首次需在客户端支持的入口审核并信任脚本，命令行使用 `/hooks`；必要时新建会话或重启。写入配置不等于桌面客户端已经运行。条件不满足时，普通路由仍能使用，只是没有自动提醒。[官方脚本机制](https://learn.chatgpt.com/docs/hooks)

## 第二步：正常输入，不需要每句话加前缀

全局设置完成后，每句话、每个新对话都像平时一样输入。不是第一次写一次前缀就永久启用，真正起作用的是上面的全局配置。

1. 输入任务。
2. 查看模型和推理强度。
3. 在 Codex 中选好推荐组合。
4. 单独发送「执行」，继续原任务。

Plus 策略示例：

```text
模型：GPT-6.1 Sol；推理强度：中
原因：任务需要多步修改，先沿用已验证的性价比方案。
操作：在模型选择器中选择模型和推理强度，然后发送“执行”。
```

只有强制要求“只推荐、不执行”时，才加对应的 `$model-router-20` 或 `$model-router`。继续复杂任务时，不能因为上一项任务用了 Luna 或 Terra 就一直沿用。

## 什么时候用哪个模型？

| 工作 | 候选 | 常用起点 |
| --- | --- | --- |
| 规则明确的机械提取、表格整理或精确替换 | GPT-6 Luna | 轻或中 |
| 范围明确的资料写作、图表与界面解读、明确的软件操作或可检查的已知修复 | GPT-6.1 Terra | 中；判断少时用轻 |
| 细节密集但边界明确的视觉工作 | GPT-6.1 Terra | 高 |
| 多步开发、资料整合及超出 Terra 边界的工作 | 6.1 或 6.2 Sol | 中；明确且容易验证时可用轻 |
| 功能联动、未知或反复失败的缺陷、跨系统追查原因 | 6.1 或 6.2 Sol | 高 |
| 特别困难的单一领域或相互影响的多种原因 | 6.1 或 6.2 Sol | 极高 |
| 真正困难的整合、协调或隐蔽错误代价高的任务 | GPT-6.2 Astra | 轻或中；高风险、难验证时用高 |

这些起点是项目策略，不是官方默认值或能力等价表。Luna 要求任务单一明确、不需要调查设计、容易验证。Terra 不负责反复失败、状态或权限联动、证据冲突及隐蔽错误代价高的工作；第一步看截图不代表整个复杂任务适合 Terra。

Astra 需要至少两个真实复杂信号，同时存在困难协调、长链条依赖或隐蔽错误风险。普通多文件或交付步骤本身不够；真正困难的任务不必先让 Sol 失败一次。

### 两个订阅策略的区别

- **ChatGPT Plus：**保留已验证的 GPT-6.1 Sol 基线。明确要求、具体能力需要，或同输入同推理强度下有总用量或返工更少的依据时，再选 6.2 Sol；不能声称 6.1 永远更便宜。
- **ChatGPT Pro：**先评估 6.2 Sol，但用户偏好、验证过的工作流或上下文计费更合适时仍保留 6.1。额度更多不代表普通任务都要用 Astra。
- **Plus 节约转换只执行一次：**基础推荐为 Astra 轻或中时，改为本次选定的性价比 Sol 极高，通常是 6.1 Sol；有上述理由时可选 6.2 Sol。Astra 高及以上改为 6.2 Astra 轻。不会把结果再转换一次，也不转换 Luna、Terra 或 Sol 的基础推荐。降低推理不代表质量等价，用户明确且可用的要求优先。
- **Pro：**不执行上述 Plus 转换，保留基础推荐。

[价格与性价比策略](docs/pricing.zh-CN.md)列出有日期的积分参考及计费区别。比较正确性、实际用量、推理、上下文缓存、得到可用结果的时间及返工，不只比较单价或版本号。

### 可用选项与上下文

本次核对的本机目录中，五个模型都有轻至最大，除 Luna 外另有超强；仍以实际选择器为准。不能把接口支持当成客户端可选项，也不能推荐本机未列出的无推理选项。超强可能委派任务，可用不等于已经得到授权。速度不动。

官方列出的 Codex 默认上下文：6.2 Astra 二十七万二千个令牌，6.2 Sol 五十万个令牌，不等于模型或接口上限。材料长不自动代表应该用 Astra；应检查容量和计费，不悄悄丢资料或改设置。Terra 已核实的命令行最低版本仍为 0.159.0，不能拿它推断 6.2 的最低版本或账号权限。[模型与上下文](https://learn.chatgpt.com/docs/models)、[6.2 推理建议](https://learn.chatgpt.com/guides/prompting-gpt-6-2-astra)

## 更新由你决定

**发布 GitHub 新版不会自动升级维护者本机。** 需要测试完整流程时保留旧版；发布与验收只使用隔离目录，不修改真实技能、全局规则、提醒或客户端设置。

使用 1.2.1 或更新版本时，单独输入「检查路由器更新」只检查；输入「更新路由器」才升级同一策略，不执行待确认任务。核实有新版时，推荐可增加第四行：

> 更新：模型路由器已有新版（版本号），输入“更新路由器”即可更新。

前台只读缓存，后台每二十四小时最多检查一次，失败也会缓存；手动检查可刷新。首次提醒可能出现在下次任务。接口限流时通过官方最新发布链接检查，不读取凭据。只有正式发布版本触发提醒，普通提交不会。

旧版或更新器不可用时，可发送：

```text
请把本机 Codex 模型路由器更新到 alanliuc-a11y/codex-model-router-gpt-6-1 的 v1.4.0。保留策略和已有标识：Plus 使用 profiles/20-usd 与 model-router-20，Pro 使用根目录与 model-router。先把旧技能及 AGENTS.md、hooks.json 备份到技能目录外，再使用不会覆盖旧目录的技能安装器重装。运行全局配置并核对版本清单和文件校验值。保留其他规则、检查脚本及提醒原来的开关状态；原本开启或我另外要求时才启用提醒。说明信任审核，不绕过审核，只保留一个生效策略。失败时恢复原安装和配置。
```

更新会校验下载、保留完整备份并恢复可捕获的安装失败。文件校验不是独立安全签名；突然退出或恢复时无法写入，可能仍需人工处理。自定义过的技能文件或 Git 克隆目录应手动升级。[测试与恢复](docs/update-testing.zh-CN.md)

不向 GitHub 发送任务或凭据，但联网会透露普通网络信息。提醒不是系统推送，也不是点击链接就能安装。没有提醒，不等于已经成功检查并确认最新。

关闭提醒：`python scripts/router-update.py disable-hooks`。路由需另外用全局脚本的 `-Disable` 或 `--disable` 关闭；预览用 `-Preview` 或 `--preview`。完整卸载前分别关闭两者。

## 历史流程截图

这些真实旧图仅展示切换与确认，不代表当前模型建议，也没有改名冒充 6.2 截图。

![旧版 Luna 示例](docs/screenshots/zh-00-luna-light-example.png)
![选择模型和推理强度](docs/screenshots/zh-01-switch-sol-high.png)
![输入执行继续](docs/screenshots/zh-02-confirm-execute.png)
![旧版 Astra 确认](docs/screenshots/zh-03-astra-confirm-execute.png)

## 验证与贡献

不承诺固定节省比例，不把旧模型成绩当作 6.2 成绩。更新器和打包测试不能证明模型推荐质量，请用[路由验收案例](docs/routing-cases.md)测试实际任务。

离线测试运行 `python -m unittest discover -s tests -v`；技能创建工具的 `quick_validate.py <技能目录>` 检查结构。发布清单由 `scripts/build-manifests.py` 生成。两个策略都附带价格及更新规则。

见[更新记录](CHANGELOG.md)、[贡献说明](CONTRIBUTING.md)、[更新验收](docs/update-testing.zh-CN.md)和 [MIT 许可证](LICENSE)。

搜索关键词：节省 Codex 令牌、节省 token、GPT-6.2 Sol、GPT-6.2 Astra、GPT-6.1 Sol 性价比、ChatGPT Plus、ChatGPT Pro、模型路由、推理强度、更新提醒。
