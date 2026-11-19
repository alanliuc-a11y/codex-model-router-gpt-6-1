# Value and subscription policy

Reviewed 2026-11-19. Read this for cost-sensitive selection, comparing Sol versions or interpreting subscription strategy. It is not a live billing dashboard.

## Separate the billing systems

ChatGPT subscription allowance, purchased credits and API-key bills are different. Do not convert API prices into included message counts or assume a per-token table predicts allowance. Use the user's actual account/seat, remaining allowance, fixed speed, effective effort, context/caching, tools, output quality and rework. Do not read secrets or infer a subscription from a dollar amount.

Official subscription families include ChatGPT Free, Go, Plus, Pro, Business, Enterprise and Edu. This release offers ready-made strategies labeled ChatGPT Plus and ChatGPT Pro. For other plans/seats, establish real availability and usage constraints first; do not silently assign the Pro strategy or promise all models are included. Keep speed settings unchanged.

## Dated reference rates

Official Codex/Work rates in credits per million tokens at Standard speed, not monthly plan prices or fixed task costs:

| Model | Input | Cached input | Output |
| --- | ---: | ---: | ---: |
| GPT-6 Luna | 2.5 | 0.25 | 12.5 |
| GPT-6.1 Terra | 25 | 1.25 | 125 |
| GPT-6.1 Sol | 50 | 2.5 | 250 |
| GPT-6.2 Sol | 50 | 2.5 | 250 |
| GPT-6.2 Astra | 200 | 10 | 1000 |

[Official credit/allowance pricing](https://learn.chatgpt.com/docs/pricing), verified 2026-11-19. Refresh before claiming these rates are still current. Both Sol versions have identical published baseline rates; neither is automatically cheaper for a complete task. The official pricing page expressly says subscription usage of GPT-6.1 Sol has no long-context surcharge. Do not infer an unverified surcharge for another model or extend that exemption to API-key usage.

Other speed modes have their own allowance/credit multipliers. Keep the user's mode and compare its applicable rates; the Standard table is a reference, not an instruction to switch speeds. Without mode/context/usage evidence, do not fabricate a numeric saving.

API-key sessions follow API pricing separately. Even when API list prices match, tool costs, long inputs and billable output can change the total. A lower-cost token rate with more retries or higher effort can cost more overall.

## Model choice

1. First eliminate unavailable combinations and models unlikely to meet the task's quality/verification requirements.
2. Use Luna/Terra only when their whole-task gates hold, not merely because their rates are lower.
3. Keep GPT-6.1 Sol as an active value candidate. Preserve a user's proven workflow instead of forcing 6.2 because it launched. On the Plus strategy, 6.1 Sol is the ordinary Sol baseline; on Pro, 6.2 Sol is a starting candidate, with 6.1 retained for proven value or preference.
4. Select 6.2 Sol when explicitly requested, concretely needed or supported by credible same-input/effective-effort comparisons that reduce total usage/rework. Equal rates permit comparison, not a blanket upgrade or a claim that 6.2 is worse.
5. Long-context subscription work makes the verified 6.1 exemption relevant. Check usable context and actual billing; do not silently discard sources, alter context settings or assume Astra has the largest default window.
6. Use Astra only when the complexity gate warrants it, then apply the chosen profile's mapping once. Pro is not a reason to use Astra for routine tasks. Explain a lower-effort quality tradeoff; if quality fails, surface the need for a stronger route.
7. Compare models at the same effective effort before lowering effort. Evaluate correctness, time to a usable result, usage and repair work on representative tasks. Estimates are not guarantees.

User experience with 6.1 Sol is valid task-specific evidence for retaining it, not proof of a universal price advantage. Official usage estimates and launch guidance can favor 6.2; neither replaces checking the user's own task and fixed settings.

## Naming and compatibility

`model-router-20` and `profiles/20-usd` are historical identifiers retained so existing installers/updaters work. They are not user-facing subscription choices. Show ChatGPT Plus / ChatGPT Pro, not price bands or assumed allowance multipliers. Changing the GitHub project title must not break the stable repository URL used by old updaters.
