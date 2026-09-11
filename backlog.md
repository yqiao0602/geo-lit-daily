# 📚 存量文献清单（backlog）— 扫描自 2024-01-01

> 候选 1007 篇 → LLM 打分 400 篇 → 收录 103 篇｜阈值 5/10｜AI 总结：正常（396/400 篇完成打分）

## 🔥 8 分以上：直接相关（48 篇）

### ⭐⭐⭐⭐ CodeGEEnius: an interpretable reasoning large language model for GEE-based geospatial code generation via distillation
**9/10** · Ziqi Liu、Shuyang Hou、Guanyu Chen、Haoyue Jiao、Shaowen Wu、Lutong Xie · Expert Systems with Applications · 2026-08-20 · [原文](https://doi.org/10.1016/j.eswa.2026.134105)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该论文提出 CodeGEEnius，通过从 DeepSeek-R1 蒸馏 19.8 万条推理式样本并构建 20 万条 SFT 样本，用 LoRA+分阶段微调 Qwen-2.5-14B，实现可解释的 GEE JavaScript 代码生成。

痛点：现有 LLM 生成 GEE 代码时在复杂任务上易偏离用户意图、且生成过程不透明，难以可信应用。方法：引入 Chain-of-Programming 机制与代码蒸馏策略，从 DeepSeek-R1 蒸馏推理导向微调数据，配合 LoRA 与分阶段微调训练 Qwen-2.5-14B。结果：在 AutoGEEval++ 的 Atomic/Combined/Theme 三个基准上 pass@5 达 94.15%/89.24%/73.56%，超越 9 个对比模型，推理内容完整性达 99.50%，并引入 LLM-as-a-Judge 评估。

> 🔗 **与课题**：与课题高度相关：(1) 同属地理空间代码生成（GEE 方向）的 NL2Code 任务，可直接作为 GEE 侧的对比基线；(2) 其 'DeepSeek-R1 蒸馏推理链 + 领域 SFT + LoRA' 流程与我的 M2（DAPT+领域指令 SFT+过程监督）和 M3（QLoRA 任务级微调基线）路线直接可比，且提供了蒸馏式过程监督数据的构造范式；(3) Chain-of-Programming 的可解释推理链思路可借鉴用于我的 L3 中间表示与分步规划可解释性设计；(4) AutoGEEval++ 提供了可参照的地理代码生成评测基准与 LLM-as-a-Judge 评测协议，可用于我的第三层'最终工作流人工可用率/可用性'评估方法设计；(5) 其'生成代码与用户意图不匹配'的痛点正是我用 KG 约束解码 + 分级回退修复要解决的问题，可作为无约束解码的对照。

### ⭐⭐⭐⭐ GISAgentBench: A Practitioner-Sourced Benchmark for Evaluating LLM Agents on GIS Tasks
**9/10** · Abhinav Pothuri、Zhe Jiang、Zelin Xu、Di Yang · arXiv · 2026-08-03 · [原文](https://arxiv.org/abs/2608.01645v1)
*来源：强命中*

**一句话**：提出 GISAgentBench——一个从 GIS Stack Exchange 收集、在真实公共数据上实例化的 349 个多步 GIS 任务基准，每个任务附带可执行参考轨迹与精确真值输出文件，用于严格评测 LLM 智能体的真实 GIS 工作流能力。

现有 GIS 智能体评测数据集多来自教材、教程或 LLM 生成种子，规模小、轨迹浅，且普遍缺少 ground truth 输出，只能依赖代码相似度、轨迹匹配或 LLM/VLM 打分等代理信号，容易把工作流形似误判为任务正确。本文构建 GISAgentBench：349 个多步 GIS 任务取自 GIS Stack Exchange，覆盖六个真实地理区域与公共数据，每任务配有可执行参考轨迹和精确真值输出文件，支持严格的容忍度感知确定性输出匹配。评测六个 LLM 后显示，最佳智能体在严格评分下仅完成 32.7% 任务，说明真实 GIS 工作流自动化仍很难。

> 🔗 **与课题**：与评测模块高度契合：其“可执行参考轨迹 + 精确真值输出 + 容忍度感知确定性匹配”正对应我三层评估中的 L3→QGIS landing 与最终工作流人工可用率，可作为可对比基线与评测协议参考；任务来源于 GIS Stack Exchange 的真实自然语言描述，可作为 M2 领域指令 SFT / 偏好数据与 NL 任务解析的数据来源，也可用于检验 M1/M3 生成工作流的顺序正确性与可执行落地率。

### ⭐⭐⭐⭐ GeoAutoModuler: a knowledge–enhanced large language model for heterogeneous geospatial code understanding and knowledge extraction
**9/10** · Jianyuan Liang、Shuyang Hou、Wenjie Chen、Yaxian Qing、Xi Zhang、Ziqi Liu · Big Earth Data · 2026-07-07 · [原文](https://doi.org/10.1080/20964471.2026.2689760)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：构建 GeoAutoModuler——一个面向异构地理空间建模脚本知识抽取的领域增强大语言模型，通过结构感知继续预训练+QLoRA 与骨架思维链指令微调完成功能模块摘要、输入输出要素识别、依赖抽取与代码片段映射。

痛点：互联网上积累的海量地理空间建模脚本语义与逻辑高度异构、非结构化，其内嵌建模知识难以被解读和复用。方法：采用结构感知的领域继续预训练（DAPT）与 QLoRA 参数高效微调提升地理代码理解能力，并用骨架思维链（SoT）领域指令微调框架分阶段完成知识抽取任务；同时构建 GeoModeling-PT/SFT/Eval 三个数据集。结果：知识抽取指标（F1、SMR-Graph、ROUGE-L、Levenshtein）较同规模模型提升 15.7%–30.8%，部分指标接近或超过 GPT-4o，原型系统验证了其在知识图谱构建、工作流可视化与地理空间代码生成上的潜力。

> 🔗 **与课题**：高度相关。①M2 路线：其“结构感知继续预训练 + 领域指令微调”与我计划的 Qwen3.5-9B-Base DAPT + 领域 SFT 流程几乎同构，可作为方法论参照与对照设计。②M3 路线：其 QLoRA 微调设置（数据组织、超参、评测口径）可直接借鉴为我的任务级 QLoRA 基线配置。③数据与评测：GeoModeling-PT/SFT/Eval 三套地理代码数据集与 F1/SMR-Graph/ROUGE-L 等指标，可为我的 L3 规划层与知识抽取类评测提供现成基准和可对比基线。④KG 模块：其“功能模块摘要—I/O 要素识别—依赖抽取—代码片段映射”的输出正是知识图谱三元组/转移合法性矩阵的上游来源，可与我的知识图谱约束解码、I/O 类型约束相衔接。⑤landing 与最终工作流：其原型支持工作流可视化与地理代码生成，与我的 L3→QGIS landing 层目标一致，但需注意它面向通用建模脚本理解，未涉及 QGIS 算子链顺序正确性与可解释回退修复，故只能部分覆盖我的评估第三层（人工可用率）。

### ⭐⭐⭐⭐ Bench4GeoCode: A Benchmark for Natural Language to Geospatial Code Generation
**9/10** · Medha Iyer、Annisa Puspa Kirana、A. de By Rolf、Mahdi Farnaghi · University of Twente Research Information · 2026-06-11 · [原文](https://doi.org/10.5281/zenodo.20645018)
*来源：强命中*

**一句话**：构建了包含100个任务、四级难度与两类鲁棒性查询的开源荷兰地理数据 NL→地理空间Python代码生成基准 Bench4GeoCode，并用功能正确性+LLM-as-Judge双协议评测了8个开源权重LLM。

痛点：LLM 生成地理空间分析 Python 代码的能力缺乏严格、标准化的评测基准，现有评测多为单步、无鲁棒性考察。方法：基于荷兰开放地理数据设计100个任务，分四个递进复杂度层级（单步数据检索→多步分析工作流），并加入含不可达需求的“陷阱查询”和需主动澄清的“歧义查询”，每个任务配套经核验的参考 Python 函数，采用自动功能评估与 LLM-as-a-Judge（评库使用与代码质量）双重协议，在统一 RAG 配置下测试4个模型家族共8个开源LLM。结果：给出各难度与鲁棒性类别的基线性能，并发现7B–27B规模内存在难以通过参数扩展、代码领域特化或MoE路由突破的组合推理天花板。

> 🔗 **与课题**：直接对应我的“评估”层，可作为 L3→QGIS landing 与最终工作流可用率评测的方法学参考与外部可对比基线：其四级复杂度对应我 IR 算子链的长度/组合难度，功能正确性自动评估可类比我的 landing 成功率与顺序正确性指标，LLM-as-Judge 代码质量评分可迁移到工作流可解释性/结构质量评估；其统一 RAG 配置与陷阱/歧义查询设计，可为 M2（DAPT+SFT 后的 Qwen）与 M3（QLoRA 基线）提供公平对比设置，歧义澄清要求也呼应我的分级回退修复与交互式澄清机制；其“组合推理天花板”结论可用于论证 KG 约束解码与 M1 自研小模型（结构化 IR+FiLM 调制+转移合法性矩阵）的必要性。

### ⭐⭐⭐⭐ GeoAgentBench: A Dynamic Execution Benchmark for Tool-Augmented Agents in Spatial Analysis
**9/10** · Bo Yu、Cheng Yang、Dongyang Hou、Chengfu Liu、Jiayao Liu、Chi Wang · arXiv · 2026-04-15 · [原文](https://arxiv.org/abs/2604.13888v1)
*来源：强命中*

**一句话**：提出 GeoAgentBench(GABench)——一个面向工具增强 GIS 智能体的动态交互式执行评测基准，含 117 个原子 GIS 工具、53 个空间分析任务、PEA 参数执行准确率指标、VLM 验证和 Plan-and-React 智能体架构。

痛点：现有 GIS LLM 智能体评测多依赖静态文本/代码匹配，忽视动态运行时反馈与多模态空间输出，无法真实反映多步地理处理工作流的执行成败。方法：构建真实执行沙箱（117 个原子 GIS 工具、6 大领域 53 个任务），提出基于 Last-Attempt Alignment 的参数执行准确率(PEA)指标，并引入 VLM 校验数据空间精度与制图风格，同时给出解耦全局编排与逐步反应执行的 Plan-and-React 架构。结果：在 7 个代表性 LLM 上的大量实验揭示了参数配置与运行时异常是任务失败主因（摘要截断）。

> 🔗 **与课题**：直接对应我的评估层（三层评估中的 L3→QGIS landing 与最终工作流可用率）：其 117 个原子 GIS 工具与 53 个空间分析任务可作为我 NL→QGIS 工作流构建的任务集与 landing 落地测试床；PEA 的 Last-Attempt Alignment 可迁移为我的「顺序正确 + 参数推断正确」自动指标；VLM 校验思路补足我当前缺失的多模态结果可用性评估；Plan-and-React 可作为 M1/M2/M3 之外的智能体式可对比基线（baseline），其运行时异常/参数错配分析也能直接指导我的分级回退修复策略设计。

### ⭐⭐⭐⭐ MiniGeoSolver: Enhancing small language models for autonomous geospatial tool sequences generation through progressive strategy
**9/10** · Jingxuan Li、Yifan Zhang、Wenhao Yu · Environmental Modelling & Software · 2026-03-28 · [原文](https://doi.org/10.1016/j.envsoft.2026.106963)
*来源：强命中*

**一句话**：提出 MiniGeoSolver，用渐进式策略增强小语言模型，使其能自主生成地理空间工具调用序列（工作流）。

痛点：大型语言模型驱动地理空间工具编排成本高、部署难，而小模型在长序列工具链规划上能力不足、顺序与类型易出错。方法：面向小语言模型设计渐进式（progressive）训练/推理策略，逐步提升其从自然语言任务描述生成地理空间工具序列的能力，实现自主、连贯的工具调用规划。结果：在环境建模与软件期刊上报告该方法显著增强了小模型的地理空间工具序列生成效果，为轻量级地理空间智能体提供了可行路径。

> 🔗 **与课题**：与课题高度重合：其'从任务描述生成地理空间工具序列'正是 L3 操作原语规划与算子链构建的核心任务，可作为 M1 路线（自研小模型+约束/修复）的直接对标工作与可对比基线；其渐进式策略可借鉴到 M2 的过程监督/课程式后训练，其评测方式可参考用于 L3 规划层与 L3→QGIS landing 的评估设计。

### ⭐⭐⭐⭐ GeoJSON agents: a multi-agent LLM architecture for geospatial analysis—function calling vs. code generation
**9/10** · Qianqian Luo、Qingming Lin、Liuchang Xu、Sensen Wu、Ruichen Mao、Chao Wang · Big Earth Data · 2026-01-18 · [原文](https://doi.org/10.1080/20964471.2026.2615511)
*来源：强命中*

**一句话**：提出 GeoJSON agents 多智能体 LLM 架构，将自然语言 GIS 任务分解为子任务，分别用函数调用与 Python 代码生成两种范式执行并迭代精化输出 GeoJSON，并构建 70 任务分级基准对比评估。

痛点：通用 LLM 缺乏 GIS 领域知识，处理复杂空间任务时精度低、稳定性差。方法：设计含任务解析、智能体协作与结果整合的多智能体框架，planner 分解任务、worker 分别通过调用预定义函数 API 或动态生成执行 Python 代码完成空间分析，并构建覆盖基础/中级/高级的 70 任务分层基准。结果：以 GPT-4o 为核心模型，代码生成路线准确率 97.14%，函数调用路线 85.x%，表明代码生成在复杂空间任务上更优。

> 🔗 **与课题**：高度相关：直接对应 NL→GIS 算子/工作流自动构建与 landing（自然语言到可执行地理操作）；其 function calling vs. code generation 对比可作为 M2/M3 路线的重要可对比基线，替代我方案中 Qwen 微调与 L3→QGIS landing 的对照；其 70 任务分级基准可参考用于三层评测（L3 规划/landing/可用率）设计与数据构建；多 agent 任务解析-协作-整合流程亦与我 IR 中间表示+算子链规划思路可对比。

### ⭐⭐⭐⭐ Bridging natural language and GIS: a multi-agent framework for LLM-driven autonomous geospatial analysis
**9/10** · Ali Mansourian、Rachid Oucheikh · International Journal of Digital Earth · 2026-01-02 · [原文](https://doi.org/10.1080/17538947.2026.2633849)
*来源：强命中*

**一句话**：该论文提出一个集成 CoT 与 RAG 的多智能体框架，将自然语言查询自动转化为可执行的 QGIS 处理算法工作流，并通过微调与自反思机制提升执行成功率。

痛点：现有 LLM 驱动的地理空间分析受限于任务执行过于简单、工具集成不足、缺乏与专业 GIS 软件交互时的上下文推理能力。方法：作者构建多智能体架构，融合思维链推理与检索增强生成，由多个专职智能体协作完成空间任务理解、地理处理工具选择与代码生成，并采用结构化微调与迭代自反思/自调试。结果：在单工具或双工具任务上执行成功率最高达 100%、语义正确率 87.5%，显著优于单智能体与未微调基线，但多步复杂工作流性能明显下降。

> 🔗 **与课题**：与课题高度相关，是直接的 NL→QGIS 工作流自动构建工作。可对照模块：(1) 作为 landing 层与端到端评测的可比基线系统（单/多智能体、微调/未微调、执行成功率与语义正确率指标可直接借用或扩展为我的三层评估中的 L3→QGIS landing 与人工可用率）；(2) 其结构化微调 + 多智能体流水线可对应我的 M2（领域 SFT/DAPT）与 M3（任务级 QLoRA 基线）；(3) 其 RAG + CoT 智能体可作为我 M1 中知识图谱约束解码与分级回退修复的对比方案（它用自反思自调试，我用 KG 转移合法性矩阵与 I/O 类型约束）；(4) 其对多步工作流性能下降的观察，正好论证我课题中引入 IR 中间表示与符号约束的必要性，可作为问题动机的文献支撑。

### ⭐⭐⭐⭐ GeoBenchX: Benchmarking LLMs in Agent Solving Multistep Geospatial Tasks
**9/10** · Varvara Krechetova、Denis Kochedykov · 预印本 · 2025-10-30 · [原文](https://doi.org/10.1145/3764915.3770721)
*来源：强命中*

**一句话**：该论文构建了 GeoBenchX 基准，用配备 23 个地理空间函数的工具调用 Agent 评测 8 个商业 LLM 在多步 GIS 任务上的表现，并提出 LLM-as-Judge 评估框架。

痛点在于缺乏标准化方法来评估 LLM 面向商业 GIS 实践者的多步地理空间工具调用能力。方法上设计四类复杂度递增的任务（含可解与故意不可解任务以测试拒答能力），用 23 个地理空间函数构建简单 tool-calling agent，并以 LLM-as-Judge 与参考答案对比。结果显示 o4-mini 与 Claude 3.5 Sonnet 综合最佳，Claude Sonnet 4 因倾向强行作答而拒答准确率低，常见错误包括几何关系误解、依赖过时知识和低效数据操作；基准集、评测框架与数据生成流水线已开源。

> 🔗 **与课题**：直接对应课题的评测层：提供了 NL→GIS 多步工作流工具调用任务的评测基准、不可解任务拒答指标与 LLM-as-Judge 自动评判方法，可用于 M2/M3 后训练模型的对比基线，也可借鉴其任务分级与错误分类（几何关系误解、过时知识、低效数据操作）来设计 L3→QGIS landing 与最终工作流可用率评估，并启发了分级回退修复中对'应拒答/不可解'情形的处理。

### ⭐⭐⭐⭐ GeoAnalystBench : A GeoAI Benchmark for Assessing Large Language Models for Spatial Analysis Workflow and Code Generation
**9/10** · Qianheng Zhang、Song Gao、Wei Chen、Yibo Zhao、Ying Nie、Ziru Chen · Transactions in GIS · 2025-10-13 · [原文](https://doi.org/10.1111/tgis.70135)
*来源：作者跟踪: Song Gao*

**一句话**：提出GeoAnalystBench基准，包含50个经专家验证的真实地理空间Python任务，从工作流有效性、结构对齐、语义相似度和代码质量四方面评估LLM的GIS工作流与代码生成能力。

针对LLM在GIS自动化中能力不明确的痛点，构建了50个真实地理空间任务基准，评估指标涵盖工作流有效性、结构对齐、语义相似度与CodeBLEU。结果显示闭源模型ChatGPT-4o-mini有效性达95%、CodeBLEU 0.39，而开源小模型DeepSeek-R1-7B仅48.5%有效性和0.272 CodeBLEU，空间关系检测与选址等深层空间推理任务最具挑战。

> 🔗 **与课题**：与课题的评测层高度相关：可作为L3规划→L3→QGIS landing→最终工作流可用率三层评估的参考基准与对比基线；其工作流有效性/结构对齐指标可迁移到QGIS工作流自动构建的评估；同时为M2（Qwen3.5继续预训练+SFT）和M3（官方后训练模型QLoRA）提供任务级对比基线，其开源/闭源模型结果可帮助定位自研模型性能。

### ⭐⭐⭐⭐ GeoGraphRAG: A graph-based retrieval-augmented generation approach for empowering large language models in automated geospatial modeling
**9/10** · Jianyuan Liang、Shuyang Hou、Haoyue Jiao、Yaxian Qing、Anqi Zhao、Zhangxiao Shen · International Journal of Applied Earth Observation and Geoinformation · 2025-07-15 · [原文](https://doi.org/10.1016/j.jag.2025.104712)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出 GeoGraphRAG，用图知识库子图检索增强 LLM 智能体，自动生成地理空间建模方案与地理处理代码。

痛点：LLM 虽具备语义理解与任务规划能力，但地理空间领域知识不足，难以直接完成地理空间建模。方法：以 LLM 为智能体识别用户需求，从外部图知识库检索相关子图，并将结构与语义信息注入 LLM，经图驱动的方案规划阶段自动产出建模方案与地理代码。结果：在自建地理空间建模基准上跨多个 LLM 与多种基线对比，验证图结构知识的注入同时提升了效率与可解释性，并给出代表性应用场景。

> 🔗 **与课题**：高度契合课题多条路线：(1) KG约束/KG增强生成——其“图知识库检索子图 + 结构/语义注入 LLM”与我 M1 路线中的知识图谱约束解码（转移合法性、I/O 类型约束）属同一 neuro-symbolic 思路，可作为 KG 增强生成的重要参考与对比；(2) landing——其“自动生成建模方案 + 地理空间代码”正对应我的 L3→QGIS landing 阶段，可对比其工具/算子组织方式；(3) eval/data——其面向地理空间建模构建的基准数据集与我三层评测（L3 规划 / landing / 人工可用率）可互参，亦可作为 baseline；(4) RAG 模块——其图 RAG 检索策略可用于我 M2 领域继续预训练与指令微调中的数据/知识注入设计。

### ⭐⭐⭐⭐ AutoGEEval: A Multimodal and Automated Evaluation Framework for Geospatial Code Generation on GEE with Large Language Models
**9/10** · Huayi Wu、Zhangxiao Shen、Shuyang Hou、Jianyuan Liang、Haoyue Jiao、Yaxian Qing · ISPRS International Journal of Geo-Information · 2025-06-30 · [原文](https://doi.org/10.3390/ijgi14070256)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出 AutoGEEval——首个面向 GEE 地理空间代码生成的多模态、单元级自动化评测框架，并构建含1325个测试用例、覆盖26种GEE数据类型的 AutoGEEval-Bench 基准，评测了18个主流LLM。

痛点：地理空间代码生成（NL2Code）方向缺乏标准化自动评测工具，模型能力难以横向对比与定量诊断。方法：基于 GEE Python API 构建 AutoGEEval 框架，把问题生成与答案验证打通为端到端流水线，从函数调用到实际执行验证，并按准确率、资源消耗、执行效率、错误类型等维度做多维量化分析。结果：在 AutoGEEval-Bench（1325 用例 / 26 类 GEE 数据类型）上评测 18 个通用、推理增强、代码专用与地学专用 LLM，揭示其性能特征与优化方向，为该领域提供统一评测协议与基础资源。

> 🔗 **与课题**：直接对应课题的评估层与 landing 环节：其‘函数调用→执行验证’的单元级评测思路可迁移到你的 L3→QGIS landing 与最终工作流可用率评测；26类数据类型/1325用例的组织方式可作为你自建 QGIS 评测基准的数据与指标设计参考；18个LLM的横向结果可作为 M2/M3 路线（领域继续预训练、指令SFT、QLoRA）在地理代码生成任务上的外部可对比基线，并可用于分析 constrained decoding/修复模块减少的具体错误类型。

### ⭐⭐⭐⭐ AutoGEEval++: A Multi-Level and Multi-Geospatial-Modality Automated Evaluation Framework for Large Language Models in Geospatial Code Generation on Google Earth Engine
**9/10** · Shuyang Hou、Zhangxiao Shen、Huayi Wu、Haoyue Jiao、Ziqi Liu、Lutong Xie · arXiv · 2025-06-12 · [原文](https://arxiv.org/abs/2506.10365v1)
*来源：强命中*

**一句话**：构建了首个面向 Google Earth Engine 地理空间代码生成的自动化多层级、多模态评测框架 AutoGEEval++，含 6365 条测试基准与执行级验证评测管线，并系统评测了 24 个大模型。

痛点：地理空间代码生成缺乏标准化自动评测工具，难以衡量 LLM 在 GEE 场景下的可用性。方法：基于 GEE Python API 构建 AutoGEEval++-Bench（26 类数据、26 种数据类型、unit/combo/theme 三类任务共 6365 用例），配提交程序与 judge 模块，实现从代码生成到执行验证的端到端自动评测，并采用准确率、资源占用、运行效率、错误类型等多维指标。结果：对 24 个通用/推理增强/代码专用/地学专用模型评测，揭示了不同任务类型、模型设计与部署方式下性能、稳定性与错误模式的显著差异。

> 🔗 **与课题**：直接对应我的『评测』模块与 GEE 自动化关注词：(1) 其三分类任务（unit/combo/theme）与我三层评估（L3 规划 / L3→QGIS landing / 最终工作流人工可用率）在分层思路上高度可对齐，可作为设计 landing 级与工作流级指标的参照；(2) 执行级自动验证(execution-based validation)+judge 模块的思路可迁移到 QGIS 工作流的可执行性与正确性自动打分；(3) 其多维度指标（准确率、资源/运行效率、错误类型）可补充为我的评估维度，尤其是算子链效率与错误模式分析；(4) 24 个 SOTA 模型结果可作为 M3 路线（官方后训练模型 QLoRA 微调基线）的对比基线参考，地学专用模型表现可佐证 M2 领域继续预训练(DAPT)的必要性；(5) 数据集构建与错误分类法可作数据模块借鉴。

### ⭐⭐⭐⭐ Design and application of a semantic-driven geospatial modeling knowledge graph based on large language models
**9/10** · Jianyuan Liang、Shuyang Hou、Anqi Zhao、Qingyang Xu、Longgang Xiang、Rui Li · Geo-spatial Information Science · 2025-04-07 · [原文](https://doi.org/10.1080/10095020.2025.2483884)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该论文提出S-GMKG，一个从4820个地理处理脚本中抽取并整合建模过程的知识图谱，用于增强LLM的地理空间建模工作流生成。

针对LLM领域知识不足导致地理分析模型生成低效、不可靠的问题，作者从众包地理处理脚本中提取功能步骤与依赖，构建语义化知识图谱S-GMKG。方法上采用骨架抽取和知识增强CoT提示自动抽取建模过程，并通过自规范化与知识增强精炼图谱，使其作为外部知识源与LLM协同生成可解释的图结构建模方案。

> 🔗 **与课题**：与课题高度相关：S-GMKG可作为KG约束/知识图谱增强生成的外部知识源，为QGIS算子链的顺序合法性、I/O类型约束和分级回退修复提供语义单元与转移依据；其从脚本抽取工作流的过程可支撑L3操作原语IR构建、M2领域数据构建与评测基准设计，并可作为KG增强LLM工作流生成的对比基线。

### ⭐⭐⭐⭐ GeoCode-GPT: A large language model for geospatial code generation
**9/10** · Shuyang Hou、Zhangxiao Shen、Anqi Zhao、Jianyuan Liang、Zhipeng Gui、Xuefeng Guan · International Journal of Applied Earth Observation and Geoinformation · 2025-03-05 · [原文](https://doi.org/10.1016/j.jag.2025.104456)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该论文开源了地理空间代码预训练/指令微调语料与评测集，并用QLoRA+LoRA基于Code Llama-7B微调出首个地理空间代码生成大模型GeoCode-GPT-7B及配套评测框架。

痛点：通用LLM因缺乏地理空间领域知识与代码语料，在GIS代码生成中易出现拒答与幻觉。方法：构建GeoCode-PT（继续预训练）、GeoCode-SFT（指令微调）与GeoCode-Eval评测集，采用QLoRA+LoRA对Code Llama-7B做两阶段训练，并建立含选项匹配、专家验证与提示工程评分的评测框架。结果：GeoCode-GPT-7B在多类任务上显著超越现有模型，选择题准确率提升9.1%~32.1%。

> 🔗 **与课题**：高度对应M2路线：其GeoCode-PT(DAPT领域继续预训练)+GeoCode-SFT(指令微调)流程可直接作为M2的数据构造与训练范式参考，Code Llama-7B+QLoRA/LoRA配置可作为M3的QLoRA微调可比基线；GeoCode-Eval及其评测框架（选项匹配+专家验证）可为你的三层评估中'代码生成质量/landing'层提供可复用的评测基准与数据来源。此外其'拒答与幻觉'问题分析与你的知识图谱约束解码、分级回退修复动机一致。

### ⭐⭐⭐⭐ Geospatial large language model trained with a simulated environment for generating tool-use chains autonomously
**9/10** · Yifan Zhang、Jingxuan Li、Zhiyun Wang、Zhengting He、Qingfeng Guan、Jianfeng Lin · International Journal of Applied Earth Observation and Geoinformation · 2024-12-20 · [原文](https://doi.org/10.1016/j.jag.2024.104312)
*来源：强命中*

**一句话**：提出GTChain框架，用种子任务引导的自指令策略在模拟环境中合成地理空间工具调用指令数据，训练开源地理空间大模型自主生成工具使用链。

痛点在于地理空间任务需多工具按序调用、规则系统不灵活，且开源LLM工具调用能力弱、商业LLM API受限难本地部署，而多步工具链的输入输出过程使指令微调数据难以收集。作者设计种子任务引导的自指令策略，在模拟环境中生成多样地理空间任务及其对应工具使用链的指令微调数据集，并据此训练开源地理空间LLM。摘要未给出定量结果，但为本地可部署的地理空间工具链生成提供了数据与训练方案。

> 🔗 **与课题**：与M2领域指令SFT高度相关：其“种子任务引导自指令+模拟环境”的数据合成方案可直接借鉴为M2的领域指令数据构造与过程监督数据来源；工具使用链生成对应本课题L3操作原语/算子链规划与L3→QGIS landing；其开源模型可作为M2/M3微调路线的可对比基线，模拟环境思路亦可支撑任务级评测与数据模块设计。

### ⭐⭐⭐⭐ GEE-OPs: An Operator Knowledge Base for Geospatial Code Generation on the Google Earth Engine Platform Powered by Large Language Models
**9/10** · Shuyang Hou、Jianyuan Liang、Anqi Zhao、Huayi Wu · arXiv · 2024-12-07 · [原文](https://arxiv.org/abs/2412.05587v2)
*来源：强命中*

**一句话**：该论文提出 GEE-OPs 框架，从 18.5 万条真实 GEE 脚本和官方语法文档中用 AST 与频繁项集挖掘抽取算子语法、算子共现频率、高频模式与关系链，构建面向 GEE JavaScript API 的地理空间算子知识库，并用 RAG 提升 LLM 的地理代码生成性能。

痛点：时空数据建模复杂度高，领域专家写码效率低、跨学科用户难以用 LLM 生成正确的 GEE 代码，且 LLM 缺乏平台算子语义与组合规律知识。方法：以 AST 解析 + 频繁项集挖掘从大规模真实脚本中抽取四类知识表（算子语法表、算子关系频率表、算子频繁模式表、算子关系链表），形成结构化算子知识库，并接入 RAG 辅助 LLM 生成。结果：算子知识抽取准确率/召回率/F1 均超 90%，接入知识库后 LLM 地理代码生成性能提升 20–30%，消融实验验证各知识表的必要性。

> 🔗 **与课题**：高度相关，直接对标本课题的“算子知识库 + 知识图谱约束 + RAG”主线：(1) 其“算子关系频率/频繁模式/关系链”表与我 L3 中间表示的算子链构造、KG 约束解码中的转移合法性矩阵高度同构，可作为 M1 知识图谱约束的构建范式与先验来源；(2) 其从大规模真实脚本自动挖掘算子使用模式的方法，可直接迁移用于 QGIS 算子语料构建，弥补 QGIS 侧缺乏 GEE 那样海量脚本的问题（对应 data/landing 模块）；(3) RAG + 算子知识库提升 20–30% 的实验结论，可作为 M2 领域继续预训练之外的“外挂知识”基线对照，用于评估 KG/RAG 与 DAPT+SFT 路线的增益差异；(4) 其算子级评测（抽取准确率、消融）为我三层评估中“L3 规划正确性”与知识表贡献度分析提供了可借鉴指标，并可作为 NL→GEE 代码生成的可对比 baseline。

### ⭐⭐⭐⭐ GIS Copilot: Towards an Autonomous GIS Agent for Spatial Analysis
**9/10** · Temitope Akinboyewa、Zhenlong Li、Huan Ning、M. Naser Lessani · arXiv · 2024-11-05 · [原文](https://arxiv.org/abs/2411.03205v4)
*来源：强命中*

**一句话**：提出 GIS Copilot 框架，把 LLM 直接接入 QGIS，让用户用自然语言驱动 agent 自动生成空间分析工作流与代码，并用 100+ 个三档复杂度任务进行评测。

痛点：生成式 AI 与成熟 GIS 平台（如 QGIS）的集成仍不充分，缺乏可自主完成空间分析的自然语言交互方案。方法：构建一个掌握 GIS 工具与参数文档知识的 LLM 推理/编程 agent，直接嵌入 QGIS，自动生成分析工作流与代码。结果：在基础与中级任务上工具选择与代码生成成功率较高，但无用户引导的高级多步任务的全自主完成仍存在明显困难。

> 🔗 **与课题**：与课题高度相关：(1) 直接对应 landing 模块——NL 任务→QGIS 工作流/PyQGIS 代码生成与平台执行；(2) 可作为 M2（领域 LLM+工具调用）与 M3（官方后训练模型微调基线）的可对比 baseline；(3) 其 100+ 任务、basic/intermediate/advanced 三档复杂度设计可借鉴为评测层（L3→QGIS landing 与人工可用率）与数据集构建参考；(4) 其'工具与参数文档注入'方式与 RAG/知识图谱约束解码（转移合法性矩阵、I/O 类型约束）思路相通，但本文缺乏显式 IR 与符号约束，正可凸显 M1 的 neuro-symbolic 可解释性优势。

### ⭐⭐⭐⭐ Geo-FuB: A Method for Constructing an Operator-Function Knowledge Base for Geospatial Code Generation Tasks Using Large Language Models
**9/10** · Shuyang Hou、Anqi Zhao、Jianyuan Liang、Zhangxiao Shen、Huayi Wu · arXiv · 2024-10-28 · [原文](https://arxiv.org/abs/2410.20975v1)
*来源：强命中*

**一句话**：该论文提出 Geo-FuB 框架，利用 15.4 万条 Google Earth Engine 脚本自动构建地理空间函数与算子的知识库，以支持 RAG 与微调范式下的地理代码生成。

痛点：通用 LLM 因缺乏地理空间领域函数与算子知识，生成的 GIS/GEE 代码常出错。方法：提出结合脚本语义的框架——函数语义框架构建(Geo-FuSE)、频繁算子组合统计(Geo-FuST)与语义映射(Geo-FuM)，使用 Chain-of-Thought、TF-IDF 与 APRIORI 算法抽取并对齐函数与算子，构建可外部检索的知识库。结果：基于 154,075 条 GEE 脚本构建的 Geo-FuB 知识库整体准确率 88.89%，结构准确率 92.03%、语义准确率 86.79%，可用于 RAG 增强与微调。

> 🔗 **与课题**：与课题高度相关：(1) 其'函数—算子'知识库可直接服务于我的 L3 平台无关操作原语 IR 层，作为 QGIS/GEE 算子语义映射与 I/O 类型约束的外部知识来源；(2) Geo-FuST 的频繁算子组合统计本质上与我 KG 约束解码中的'转移合法性矩阵'同构，可作为算子链顺序合法性先验；(3) 其 RAG + 外部知识库思路可支撑我的 KG 增强生成与 M2 领域继续预训练/指令 SFT 的数据构造；(4) 154K GEE 脚本知识库与函数对齐方法可作为我三层评测中 L3 规划层与 landing 层的领域数据/对照基线，并用于衡量算子映射覆盖度与可解释性。

### ⭐⭐⭐⭐ GeoCode-GPT: A Large Language Model for Geospatial Code Generation Tasks
**9/10** · Shuyang Hou、Zhangxiao Shen、Anqi Zhao、Jianyuan Liang、Zhipeng Gui、Xuefeng Guan · arXiv · 2024-10-22 · [原文](https://arxiv.org/abs/2410.17031v2)
*来源：强命中*

**一句话**：该论文开源了地理空间代码预训练/指令语料与评测集，并用 QLoRA/LoRA 微调 Code Llama-7B 得到首个地理空间代码生成专用模型 GeoCode-GPT-7B。

痛点：通用 LLM 在地理空间代码生成中因缺乏领域知识与代码语料而出现拒答或幻觉。方法：构建并开源 GeoCode-PT 预训练语料、GeoCode-SFT 指令语料与 GeoCode-Eval 评测集，基于 Code Llama-7B 用 QLoRA/LoRA 做领域预训练与微调，并提出选项匹配、专家验证与提示工程打分相结合的评测框架。结果：GeoCode-GPT 在多项选择准确率、代码摘要与代码生成能力上分别较其他模型提升 9.1%–32.1%、1.7%–25.4% 与 1.2%–25.1%。

> 🔗 **与课题**：直接对应 M2 路线（领域继续预训练 DAPT + 领域指令 SFT）与 M3 路线（官方/开源基座模型的任务级 QLoRA 微调基线，本文即为 Code Llama-7B QLoRA 基线）；其 GeoCode-PT/SFT 语料可作为领域数据构建参考（data），GeoCode-Eval 及其三层式评测思路（选项匹配/专家验证）可为我的三层评估（L3 规划→landing→人工可用率）提供可对比基线与评测设计借鉴。与 M1（自研编码解码+KG 约束）和 landing 模块关联较弱，但整体属于同赛道 geospatial code generation 的可对比工作。

### ⭐⭐⭐⭐ Can Large Language Models Generate Geospatial Code?
**9/10** · Shuyang Hou、Zhangxiao Shen、Jianyuan Liang、Anqi Zhao、Zhipeng Gui、Rui Li · arXiv · 2024-10-13 · [原文](https://arxiv.org/abs/2410.09738v2)
*来源：强命中*

**一句话**：该论文提出 GeoCode-Eval 评测框架与 GeoCode-Bench 基准，系统评估多种 LLM 的地理空间代码生成能力，并微调 Code LLaMA-7B 得到 GEE 领域的 GEECode-GPT。

针对地理空间代码生成中领域知识不足和“编码幻觉”等痛点，作者构建了覆盖认知记忆、理解解释、创新创造三个维度、八个能力等级的评测框架与包含选择题、填空、判断和主观任务的 GeoCode-Bench。论文评测了闭源、开源通用及专用代码模型，并比较 few-shot、zero-shot、CoT、多数投票等策略，还基于 GEE JavaScript 微调 Code LLaMA-7B 得到 GEECode-GPT。结果表明，领域预训练与指令数据构建能显著提升地理空间代码生成效果。

> 🔗 **与课题**：该论文与课题高度相关：其 GeoCode-Bench 可作为 geospatial code generation 的评测基准与可对比基线，支撑你的评测层设计；其 GEE 领域微调 GEECode-GPT 与 M2 领域继续预训练/SFT、M3 任务级微调路线直接可比；其能力维度划分也可启发 L3 规划与 L3→QGIS landing 的评测指标设计。

### ⭐⭐⭐⭐ A Comprehensive Survey of Agentic AI for Geospatial Data
**8/10** · Mohammad Hashemi、Hossein Amiri、Andreas Züfle · Preprints.org · 2026-08-12 · [原文](https://doi.org/10.20944/preprints202601.2236.v2)
*来源：领域×任务*

**一句话**：系统综述了面向地理空间数据的智能体（Agentic AI）研究，提出覆盖地理数据模态、智能体核心能力与应用场景的统一分类体系，并附带论文清单仓库。

痛点在于地理空间任务天然多模态、受时空约束、且需与 GIS 库、地图服务、对地观测流水线等外部资源可靠交互，单次生成的 LLM 难以胜任。该文综述了以 LLM 为内核、结合推理与工具调用行动的 agentic AI 在地理空间智能中的进展，提出统一分类法（数据模态 / 智能体能力 / 应用领域：地理分析、遥感、城市规划、出行）。结果为领域提供了一张系统性的研究地图与公开论文列表（GitHub awesome 列表）。

> 🔗 **与课题**：高度相关但属综述而非方法：可为课题的 GIS agent/copilot、工具调用、workflow 自动构建提供系统的相关工作梳理与定位框架；其“GIS 库/地图服务/EO 流水线作为外部资源”的划分直接对应我的 L3→QGIS landing 与工具调用环节；分类法中的能力维度可用于组织评测维度（三层评估中 L3 规划与 landing 的指标设计）；论文清单可作为数据/基准与可对比基线的检索入口（如已有 GIS 智能体基准、NL2Geo 工具调用工作）。不涉及 M1 的 IR/FiLM/KG 约束解码，也不提供 M2/M3 的微调方法。

### ⭐⭐⭐⭐ GEEToker: you can boost LLMs’ JavaScript-based geospatial code generation for Google Earth Engine with a model-agnostic tokenizer
**8/10** · Shuyang Hou、Haoyue Jiao、Ziqi Liu、Jianyuan Liang、Lutong Xie、Xuefeng Guan · International Journal of Geographical Information Systems · 2026-08-03 · [原文](https://doi.org/10.1080/13658816.2026.2700394)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该文提出 GEEToker——一个模型无关、可迁移的分词器构建框架，通过数据规范化、种子词元挖掘与词表增强训练，提升 LLM 生成 Google Earth Engine JavaScript 地理空间代码的能力。

痛点：通用分词器对 GEE 领域语法切分不准，导致训练与推理中的生成幻觉，且 GEE 代码开发门槛高。方法：构建模型无关的分词器优化框架（数据规范化+种子词元挖掘+词表增强训练），并发布 GEE-PT、GEE-SFT、GEEtokenization-Bench、GEE-Bench 等数据集。结果：词元消耗降低 46.47%–53.78%，覆盖率提升 2.08%–17.82%，训练/推理时间缩短 4.20%–28.84%，实体抽取、代码生成与补全任务提升 2.02%–20.00%。

> 🔗 **与课题**：与课题高度相关：1) 属 GIS 代码生成（GEE 侧）与 NL2Code 范畴，可作为 landing 阶段 GEE 平台映射与评测的对比基线；2) 其领域分词器/词表增强思路可迁移到 M2 路线（Qwen3.5-9B-Base 领域继续预训练前的领域词表适配）；3) 发布的 GEE-PT/GEE-SFT 指令数据与 GEE-Bench 评测基准可为本课题的领域数据构造与三层评估（尤其 L3→平台 landing 与最终可用率）提供数据与评测参考；4) 模型无关的分词器框架与 L3 操作原语 IR 的平台无关思路相通，可启发跨平台（GEE/QGIS）统一语义层的词元设计。

### ⭐⭐⭐⭐ PostGISer: The first end-to-end fine-tuned large language model for PostGIS GeoSQL query generation
**8/10** · Shuyang Hou、Ziqi Liu、Lutong Xie、Guanyu Chen、Haoyue Jiao、Shaowen Wu · Information Processing & Management · 2026-07-08 · [原文](https://doi.org/10.1016/j.ipm.2026.105042)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该论文构建并端到端微调了首个面向 PostGIS 空间 SQL（GeoSQL）生成的大语言模型 PostGISer，实现自然语言到空间数据库查询的直接转换。

痛点：空间 SQL 查询编写门槛高，通用 LLM 缺乏 PostGIS 几何函数与空间语义的专门知识，现有方法多依赖多阶段流水线或提示工程而非端到端微调。方法：作者构建领域数据集并对基座 LLM 做端到端微调，使其直接从自然语言任务描述生成可执行的 PostGIS GeoSQL。结果（据标题/摘要定位）：成为首个端到端微调的 PostGIS GeoSQL 生成模型，在空间查询生成任务上取得优于通用模型的可用性。

> 🔗 **与课题**：与 M2 路线（Qwen3.5-9B-Base 领域继续预训练 + 领域指令 SFT）直接同构，可作为地理领域 NL2Code 微调的重要参照与可对比基线；其数据构造方式可为我的 L3→QGIS landing 数据集提供参考（自然语言→空间算子/SQL 的映射监督）；同时其空间函数语义知识可作为 KG 约束解码中 I/O 类型与算子合法性矩阵的语料来源。与评测层相关：可作为 NL2Code/GeoSQL 任务的对比基线之一。

### ⭐⭐⭐⭐ From questions to queries: an AI-powered multi-agent framework for spatial text-to-Sql
**8/10** · Ali Khosravi Kazazi、Zhenlong Li、M. Naser Lessani、Guido Cervone · International Journal of Digital Earth · 2026-07-01 · [原文](https://doi.org/10.1080/17538947.2026.2687193)
*来源：作者跟踪: Zhenlong Li*

**一句话**：提出一个多智能体空间 Text-to-SQL 框架，通过分阶段语义解析、schema 落地、逻辑规划、SQL 生成与基于执行的审查，并发布 SpatialQueryQA 空间查询评测基准。

痛点：PostGIS 的空间语义（地理意图、几何字段、空间函数选择、CRS 与度量假设）使空间 Text-to-SQL 比通用 Text-to-SQL 更易出错，非专家难以使用。方法：将任务分解为多个紧耦合智能体（解释、schema grounding、逻辑规划、SQL 生成、执行审查），并以程序化 schema 画像、语义增强与向量检索构建知识库支撑。结果：KaggleDBQA 达 81.2%、新基准 SpatialQueryQA 达 87.7%（无审查阶段为 76.7%），说明分解+执行审查显著提升空间敏感查询鲁棒性。

> 🔗 **与课题**：高度相关。其多智能体分阶段流水线（schema grounding→逻辑规划→代码生成→执行审查回修）可作为 M2/M3 路线在空间 NL2Code 任务上的可对比基线与架构参照；知识库的程序化 schema 画像+语义增强+embedding 检索对应我的 RAG/KG 约束与 I/O 类型约束模块；'执行审查纠错'与我的分级回退修复机制直接对应；SpatialQueryQA 基准与分层次、覆盖导向的评测设计可借鉴到我的 L3 规划/L3→landing/人工可用率三层评测体系，尽管它是 SQL 而非 QGIS 工作流落地。

### ⭐⭐⭐⭐ GeoCode Forge: An Intelligent Assistant for Google Earth Engine
**8/10** · LuojiaGeoCode、Shaowen Wu、Shuyang Hou、Ziqi Liu、Haoyue Jiao、Lutong Xie · Zenodo (CERN European Organization for Nuclear Research) · 2026-05-22 · [原文](https://doi.org/10.5281/zenodo.21550004)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该论文构建了 GeoCode Forge——一个面向 Google Earth Engine 的自然语言编程助手，可实现意图识别、需求澄清、数据集推荐、GEE JavaScript 代码生成并注入 Code Editor，以及运行时错误检测与修复。

痛点在于 GEE 遥感分析工作流门槛高、需手工编写 JavaScript 并反复调试。方法上以 LLM 为核心，串联意图识别（新任务/改需求/调试/问答）、交互式需求澄清（数据集、区域、时间范围）、卫星数据集推荐、可执行代码生成与直接注入 GEE Code Editor，并提供上下文感知的报错检测与修正，支持 Claude/GPT/Gemini/Qwen/Ollama 多模型后端。结果是一个端到端的自然语言到 GEE 代码的可运行助手系统。

> 🔗 **与课题**：与课题高度相关：同属 geospatial code generation / GIS copilot 与 NL2Code 方向，且面向 GEE 自动化（对应我关注的 GEE 算子映射与 landing）。其"意图识别+交互式需求澄清+数据集推荐"可作为需求理解与上下文补全模块的参考（对应 RAG/数据选择）；"代码注入 Code Editor + 运行时错误检测与纠错"与我的 L3→QGIS landing 及分级回退修复模块直接对应，可作为 M3 任务级微调基线的对照系统；其澄清式交互也是评估"最终工作流人工可用率"时可借鉴的评测维度。不足之处是未涉及 IR/原语中间表示、知识图谱约束解码与 DPO 训练，故对 M1 的 KG 约束与 M2 的后训练部分借鉴有限。

### ⭐⭐⭐⭐ An Automated Framework for Natural Language-Based Spatial Query Using Large Language Models
**8/10** · Ensiyeh Javaherian Pour、Yiqun Chen、Alice Kesminas、Abbas Rajabifard、Mazdak Ghasemi Tootkaboni · Journal of Geovisualization and Spatial Analysis · 2026-04-27 · [原文](https://doi.org/10.1007/s41651-026-00260-9)
*来源：领域×任务*

**一句话**：提出基于LLM多智能体流水线的空间查询与分析（SQA）框架，将自然语言查询自动翻译为经校验、可执行的空间操作并支持动态知识增强。

痛点在于空间分析自动化依赖预定义工作流、静态schema和专家配置，难以跨数据集与场景迁移。方法上框架先用LLM区分一般查询与空间查询，空间查询走多智能体流水线（语义解析、空间分析、同行评审式验证、代码执行检查），并通过动态知识增强支持用户上传新数据集的自动校验与集成，另含两步式错误恢复机制。结果在大城市校园数据集上，其空间推理表现优于单智能体基线（含带元数据访问与纠错机制的配置）。

> 🔗 **与课题**：与课题的landing与修复模块高度相关：其'N自然语言→经验证的可执行空间操作'正是L3→落地执行的映射问题，其多智能体验证+代码执行检查对应工作流的顺序/类型正确性校验；'两步错误恢复'与自研M1路线的分级回退修复思路可直接对照；该文以LLM（M2/M3路线范式）为基座做领域化空间任务落地，可作为M2/M3的应用型对比基线；其单智能体 vs 多智能体的消融与校园数据集评测，可借鉴到三层评测体系（L3规划/landing/可用率）的基准构建中；但未涉及QGIS算子链、IR中间表示与KG约束解码，属于互补而非重叠工作。

### ⭐⭐⭐⭐ Geochain AI: Automated Spatial Analysisusing Large Language Models and Chain of Thought
**8/10** · Dr.Dhivya P.、Dr.Akila S.、. Divya S、Amarnath. S、Afzal . A · International Scientific Journal of Engineering and Management · 2026-03-31 · [原文](https://doi.org/10.55041/isjem05858)
*来源：强命中*

**一句话**：提出 Geochain AI 框架，用 LLM 配合思维链(CoT)与 RAG 检索工具文档，把自然语言空间分析请求自动分解并编排为 ArcPy/GDAL/GeoPandas 地理处理任务序列。

痛点：传统空间分析依赖 GIS 专家在 ArcGIS/QGIS 中手动逐条执行地理处理工具，流程构建低效且难以复用。方法：以 LLM 做 CoT 任务分解，用 RAG 模块检索 ArcPy、GDAL、GeoPandas 等相关文档来支撑子任务的算子选择与执行编排，实现端到端的地理处理工作流自动生成。结果：论文声称该框架能针对地理空间问题自动完成分析流程编排，但属较初期工程性工作，缺少严谨的基准评测与可靠性分析。

> 🔗 **与课题**：与课题高度同源：同样做'自然语言→地理处理算子链'的任务分解与工具编排，可作为 M3（官方后训练模型任务级微调基线）之外最直接的 LLM+CoT+RAG 对比基线，其 RAG 检索工具文档的思路也可对照你的 KG 约束解码与分级回退修复模块；但它只到任务分解+工具调用层面，未涉及 L3 中间表示、转移合法性/I-O 类型约束解码、顺序正确性保证与 landing 到 QGIS 的可执行验证，也没有规范的评测基准，正好是你工作要补的空缺。

### ⭐⭐⭐⭐ GeoAgentic-RAG: A Multi-Agent framework for autonomous geospatial reasoning and visual insight generation with LLM
**8/10** · Chao Liang、Yuanzheng Cui、Run Shi、Guixiang Zha、Xin Yin、Mingzhong Xiao · International Journal of Applied Earth Observation and Geoinformation · 2026-02-20 · [原文](https://doi.org/10.1016/j.jag.2026.105195)
*来源：强命中*

**一句话**：提出 GeoAgentic-RAG 多智能体框架，融合 RAG 与 LLM 实现地理空间自主推理、可执行空间分析与可视化洞察生成。

痛点在于传统文本相似度 RAG 无法表达拓扑与空间上下文等空间语义，导致地理问答效果受限。作者构建多智能体框架，集成自然语言查询解析、语义-空间检索、矢量/栅格/多模态统一数据库与可执行地理分析任务分解，让多个专职 agent 协同生成可解释分析结果。在南京、广州的检索、要素刻画与空间关系推理基准上取得 85.3% 通过率与 88.3% 答案正确率。

> 🔗 **与课题**：与课题高度相关的 LLM+多智能体+可执行地理分析路线，可作为 M2 路线（领域 LLM agent）以及 L3→QGIS landing 的对照/对比基线；其语义-空间检索与任务分解模块对应 RAG/知识增强与工作流规划，其基准与通过率、正确率指标可借鉴到我的三层评测（L3 规划 / landing / 人工可用率）中。

### ⭐⭐⭐⭐ NeoSpatial: Agentic AI Driven Solution, Revolutionizing Oil and Gas Exploration Geospatial Workflows
**8/10** · Q. Hassan、A. Rahman、M. A. Majid、F. Tayyab、R. Fadul · 预印本 · 2026-01-13 · [原文](https://doi.org/10.2523/iptc-25209-ms)
*来源：强命中*

**一句话**：提出 NeoSpatial——一个结合 LLM 推理、ReAct GIS 智能体与策略护栏的自主平台，把自然语言指令翻译为可执行、合规的 ArcGIS 地理处理工作流并自动确定算子执行顺序。

痛点：油气勘探需要快速整合分析多源地理空间数据，传统规则式自动化难以覆盖复杂流程，且对用户地理知识要求高。方法：用 LangChain/LangGraph 做编排、ArcGIS Python API 做空间计算、ReAct 智能体嵌入地理工具，并加入 policy guardrails 与 human-in-the-loop 实现全自主模式下的有序地理处理任务链生成。结果：已支持井位规划、基础设施选线、区域筛选与盆地评价、圈闭刻画等企业级工作流自动化，并接入企业智能信息检索。

> 🔗 **与课题**：与课题高度同构：同样是『自然语言任务描述→自动构建顺序正确的地理处理算子链』，可作为 M2/M3 之外的重要对比基线（agentic+ReAct+编排框架路线）与相关工作。可借鉴点：任务顺序自动确定（对应 L3 规划的算子序列生成）、策略护栏（对应 KG 约束解码/合法性矩阵的思想）、human-in-the-loop 与人工可用率评测（对应你的第三层评估）。差异：其落地平台是 ArcGIS 而非 QGIS，且偏工具编排工程实现而非 L3 中间表示与自研模型；可为 landing 层与评测设计提供参照。

### ⭐⭐⭐⭐ Geospatial Knowledge-Base Question Answering Using Multi-Agent Systems
**8/10** · Jonghyeon Yang、Jiyoung Kim · ISPRS International Journal of Geo-Information · 2026-01-08 · [原文](https://doi.org/10.3390/ijgi15010035)
*来源：领域×任务*

**一句话**：提出基于GPT-4o的多智能体提示框架，将地理知识库自然语言问题翻译为可执行GeoSPARQL，并引入算子感知的中间表示与OSM/GeoSPARQL算子检索接地。

痛点：GeoKBQA此前依赖手工规则、缺乏规范的数据划分与公平评测。方法：构建意图分析器、多粒度检索器（把概念/属性接地到OSM标注模式、关系映射到GeoSPARQL/OGC算子清单）、算子感知中间表示与查询生成器的多智能体流水线，仅用每智能体20个少样本示例。结果：GeoKBQA测试集上达85.49 EM，优于在3574条数据上微调的基线，且多智能体比单智能体提升显著（大模型收益更大）。

> 🔗 **与课题**：高度相关。(1) 'operator-aware intermediate representation aligned with SPARQL/GeoSPARQL 1.1' 与我的 L3 平台无关操作原语IR思路同构，可作为L3设计的对照与论据；(2) 多粒度检索器把概念/关系接地到OSM tagging schema与OGC/GeoSPARQL算子清单，对应我的KG约束解码与RAG接地模块，可比较'检索接地'与'知识图谱合法性矩阵/类型约束'两条路线的优劣；(3) NL→GeoSPARQL 属于NL2Code/geo-query生成，其landing目标（可执行查询语言）可与我L3→QGIS landing做类比，是跨平台的落地范式参照；(4) 少样本多智能体GPT-4o(85.49 EM)是M2/M3路线在geo领域的强prompt基线，可作对比基线；(5) 其GeoKBQA测试集与EM评测协议可纳入我的评测层，尤其'数据集划分公平性'的批评直接适用于我的三层评估设计。

### ⭐⭐⭐⭐ From tool to collaborator: rethinking GIScience as GIS becomes agentic and autonomous
**8/10** · Ali Khosravi Kazazi、Zhenlong Li · International Journal of Digital Earth · 2026-01-02 · [原文](https://doi.org/10.1080/17538947.2026.2687228)
*来源：作者跟踪: Zhenlong Li*

**一句话**：该文综述并理论化了GIS从工具走向自主智能体后，规划、工作流构建与运行时方法修订带来的验证与治理挑战，提出Agentic Role Entanglement模型和验证栈。

痛点：传统GIS范式假设系统只执行人类预先编写的命令，而agentic/autonomous GIS开始解释意图、构建并迭代修改工作流，使原有验证与同行评审假设失效。方法：通过整合性叙事综述，提出Agentic Role Entanglement模型，把工具使用、运行时方法构建和认知探究耦合到同一分析事件中，并给出以溯源、可复现性、工作流、代码验证、地理空间合理性检查和不确定性限定声明为核心的验证栈。结果：主张以人-智能体系统为分析单元，推动后工具主义GIScience在科学可辩护性、透明性和问责制方面建立新评价与治理框架。

> 🔗 **与课题**：与课题高度相关，尤其对应GIS agent/copilot、自然语言意图到工作流自动构建、运行时工作流修订与可解释性验证。可为评估层（L3规划、L3→QGIS landing、最终人工可用率）提供理论框架与验证指标参考，如溯源、可复现性、工作流正确性、代码验证和geospatial sanity checks；也可作为GIS agentic autonomy方向的综述性引用与评估设计基线，但不直接涉及M1的BERT+Transformer+FiLM、M2领域预训练、M3 QLoRA或KG约束解码。

### ⭐⭐⭐⭐ ShapefileGPT: a multi-agent large language model framework for automated shapefile processing
**8/10** · Qingming Lin、Rui Hu、Huaxia Li、Sensen Wu、Yongdan Li、Kai Fang · International Journal of Digital Earth · 2025-11-14 · [原文](https://doi.org/10.1080/17538947.2025.2577884)
*来源：领域×任务*

**一句话**：提出 ShapefileGPT——一个由 planner 与 worker 组成的多智能体 LLM 框架，通过函数调用自动完成 Shapefile 矢量数据的空间分析任务。

痛点是矢量地理数据处理门槛高、需领域专家知识，而通用 LLM 难以应对 GIS 矢量数据固有的空间拓扑复杂性。方法上采用 planner(任务分解与监督)+worker(空间算子执行)的多智能体架构，并自建带 API 文档的空间分析库以实现函数调用式操作。基于权威教材构建了几何运算、空间查询等类别的评测数据集，任务成功率达 95.24%，显著优于通用 GPT 模型。

> 🔗 **与课题**：与课题高度相关：(1) 属于 GIS agent/copilot + 工具调用的代表性工作，可作为 M2/M3 路线(LLM 驱动的 GIS 自动化)的对比基线；(2) planner-worker 的任务分解+算子执行结构与我的 L3 操作原语/算子链构建目标同构，其函数调用接口设计可对照我的 L3→QGIS landing 层设计；(3) 其基于教材自建的评测数据集与任务级成功率指标，可为我的第三层评估(最终工作流可用率)提供数据与评测方法参考；(4) 其暴露的 LLM 在空间拓扑约束上的失败模式，正是我用 KG 约束解码与分级回退修复要解决的问题。缺点是不涉及 IR 语义层、约束解码与微调。

### ⭐⭐⭐⭐ GeoColab: an LLM-based multi-agent collaborative framework for geospatial code generation
**8/10** · Huayi Wu、Haoyue Jiao、Shuyang Hou、Jianyuan Liang、Zhangxiao Shen、Anqi Zhao · International Journal of Digital Earth · 2025-11-06 · [原文](https://doi.org/10.1080/17538947.2025.2569405)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出首个面向地理空间代码生成的多智能体协作框架 GeoColab，通过角色分工与知识库/RAG 支持提升 LLM 生成代码的可执行性与准确率，并发布 GeoCodes 评测基准。

痛点：LLM 直接做地理空间代码生成时存在需求解析、语法适配、路径检索、代码验证与空间识别等困难，易产生'代码幻觉'。方法：定义产品经理、算法工程师、程序员三个智能体角色并标准化流程，集成包含 8729 个函数语法文档、2732 个数据集、115 个外部 API、94 种投影方法与 3837 条 CRS 转换记录的知识支持机制与 RAG。结果：在 GPT-4.5、DeepSeek-V3 等七个主流 LLM 上代码可执行性/准确率/可读性提升 7.59%–26.09%，超过 CodeCoT、ChatDev 等基线最多 31.03%，消融显示去掉知识模块性能下降 4.39%–9.30%。

> 🔗 **与课题**：与课题高度相关：(1) 同为'自然语言→地理空间代码/工作流自动生成'任务，可作为 M1/M2/M3 路线在 GIS 代码生成上的可对比基线系统；(2) 其知识库+RAG 机制与我 KG 约束解码/RAG 增强思路互补，可作为 KG/检索增强模块的参照实现；(3) GeoCodes 基准（25 显式+15 不完整+10 开放式任务）可用于评测层，尤其在'L3 规划正确性'与'landing 到真实 GIS 算子/API'的可用率评估上可借鉴其任务分类与指标体系；(4) 空间识别与代码验证环节对应我的 landing 阶段与分级回退修复机制；差异在于其面向多智能体+通用代码生成，未涉及平台无关 IR、转移合法性矩阵与顺序正确性约束。

### ⭐⭐⭐⭐ Extraction of geoprocessing modeling knowledge from crowdsourced Google Earth Engine scripts by coordinating large and small language models
**8/10** · Anqi Zhao、Zhipeng Gui、Jianyuan Liang、Yuhang Liu、Dehua Peng、Wenzhang Wei · International Journal of Geographical Information Systems · 2025-11-03 · [原文](https://doi.org/10.1080/13658816.2025.2577252)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出 Geo-CLASS 框架，协同大模型与小模型从 23.7 万条众包 GEE 脚本中抽取地理处理建模知识，以支撑地理处理建模知识图谱构建与 RAG 驱动的脚本生成。

痛点：GEE 等平台积累的海量众包脚本蕴含地理处理工作流知识，但 SLM 难以理解复杂代码、LLM 缺乏一致的地学术语，导致知识抽取的实体与关系表达不规范。方法：设计领域专用 schema 与 schema-aware 提示策略引导 LLM 生成并关联实体描述，再用 SLM 将描述映射到构建的地学知识库完成标准化，形成大-小模型协同的知识抽取框架。结果：在从 295,943 条脚本中筛选出的 237 条 GEE 脚本上，实体与关系识别准确率较 Llama-3、GPT-3.5、GPT-4o 等基线最高提升 31.9% 与 12.0%，并可支持建模知识图谱构建、领域推理与 RAG 脚本生成。

> 🔗 **与课题**：与课题高度相关：(1) 数据/语料模块——提供 GEE 众包脚本的知识抽取方法与脚本筛选流程，可用于构建 QGIS/GEE 跨平台工作流语料与 IR 映射标注；(2) KG 模块——其 schema 化实体-关系抽取直接对应 L3 操作原语与知识图谱构建，可作为 KG 约束解码的知识来源；(3) RAG 模块——论文明确指向用抽取知识支撑 RAG 脚本生成，可对标 M1/M2 中的知识增强生成路线；(4) baseline——其 LLM 抽取基线（Llama-3/GPT-3.5/GPT-4o）与评测协议可作为知识抽取环节的对比基线。

### ⭐⭐⭐⭐ GeoFlow: Agentic Workflow Automation for Geospatial Tasks
**8/10** · Amulya Bhattaram、Justin Chung、Stanley Chung、Ranit Gupta、Janani Ramamoorthy、Kartikeya Gullapalli · 预印本 · 2025-11-03 · [原文](https://doi.org/10.1145/3748636.3763217)
*来源：领域×任务*

**一句话**：提出GeoFlow方法，为每个智能体指定详细的工具调用目标，自动生成地理空间任务的智能体工作流。

现有工作侧重推理分解而忽略API选择的显式指导，导致地理空间任务工作流生成效果不佳。GeoFlow通过为每个智能体提供详细的工具调用目标来引导地理空间API调用，在主流LLM系列上比SOTA提升6.8%成功率并减少最多4倍token消耗。

> 🔗 **与课题**：与M2/M3路线直接相关：都使用LLM进行地理空间工作流生成与工具调用规划，可作为agentic workflow自动化基线对比；其工具调用目标设计可借鉴于landing阶段的API映射与评测设计，但未涉及IR/KG约束解码。

### ⭐⭐⭐⭐ GeoCogent: an LLM-based agent for geospatial code generation
**8/10** · Shuyang Hou、Haoyue Jiao、Jianyuan Liang、Zhangxiao Shen、Anqi Zhao、Huayi Wu · International Journal of Geographical Information Systems · 2025-08-22 · [原文](https://doi.org/10.1080/13658816.2025.2549460)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出基于LLM的GIS代码生成智能体框架GeoCogent，集成规划、工具增强推理与记忆机制，并开源GeoCodes评测基准。

痛点：现有LLM做地理空间代码生成时在需求解释、语法适配、路径检索与验证上不足，易产生不可读/不可运行的"代码幻觉"。方法：GeoCogent融合任务规划、工具增强推理与记忆机制，实现需求理解、动态知识检索和上下文一致性维护。结果：在显式、不完整、开放式需求下均高效，各机制消融贡献显著，原型支持本地部署与LLM接入，并开源了带评价指标的GeoCodes基准。

> 🔗 **与课题**：高度相关：可作为M2/M3路线（LLM领域继续预训练与指令微调）的对比基线，其规划+工具调用+知识检索架构与我的工作流算子链规划、RAG增强、级联修复思路对应；GeoCodes基准可用于我的L3规划层与最终工作流可用率评估参考；其本地部署与LLM集成设计对QGIS landing有借鉴价值（但未涉及QGIS算子级IR与知识图谱约束解码，正是我课题的差异化空间）。

### ⭐⭐⭐⭐ Chain-of-programming (CoP): empowering large language models for geospatial code generation task
**8/10** · Shuyang Hou、Haoyue Jiao、Zhangxiao Shen、Jianyuan Liang、Anqi Zhao、Xiaopu Zhang · International Journal of Digital Earth · 2025-05-27 · [原文](https://doi.org/10.1080/17538947.2025.2509812)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：提出Chain-of-Programming (CoP)五步框架(需求分析→算法设计→代码实现→调试→注释),结合共享信息池、知识库检索与用户反馈,实现无需微调的地理空间代码生成。

痛点:LLM做地理空间代码生成时面临用户需求不完整、平台特定语法知识不足,导致'代码幻觉'。方法:CoP将生成拆为五个步骤,引入共享信息池、知识库检索和用户反馈,免微调端到端生成。结果:在地理问题分类与评测基准上,代码逻辑清晰度、语法正确性、可执行性提升3.0%~48.8%,并通过对比/消融实验与建筑可视化、火灾数据分析案例验证,开源了原型系统。

> 🔗 **与课题**：高度相关。1) 思路与本课题'分步规划+知识约束+修复'一致,可作M1/M2的prompt/流程式对比基线;2) 知识库检索对应你的RAG/KG增强生成模块,L3知识图谱约束可与其知识库检索对比;3) 五个步骤(需求分析/算法设计/实现/调试/注释)对应你的L3规划→landing→修复分级回退链路,可借鉴其信息池设计;4) 其地理问题分类与评测基准可直接用于你的L3规划层与最终工作流可用率评测,并作为无微调基线与M3 QLoRA基线对照。

### ⭐⭐⭐⭐ AutoGEEval: A Multimodal and Automated Framework for Geospatial Code Generation on GEE with Large Language Models
**8/10** · Shuyang Hou、Zhangxiao Shen、Huayi Wu、Jianyuan Liang、Haoyue Jiao、Yaxian Qing · arXiv · 2025-05-19 · [原文](https://arxiv.org/abs/2505.12900v1)
*来源：强命中*

**一句话**：提出AutoGEEval——首个面向GEE地理空间代码生成的多模态、单元级自动化评测框架，并构建含1325个测试用例、覆盖26种GEE数据类型的基准AutoGEEval-Bench，对18个LLM进行多维度评测。

痛点：地理空间代码生成（NL→GEE代码）缺乏标准化自动评测工具，难以公平比较模型能力。方法：基于GEE Python API构建题目生成+答案验证的端到端自动化流水线，从函数调用到执行验证全过程校验，并从准确率、资源消耗、执行效率、错误类型等维度量化分析。结果：评测18个通用/推理增强/代码专用/地学专用LLM，揭示其性能特征与优化路径，为NL2领域代码翻译提供统一协议与基础资源。

> 🔗 **与课题**：直接对应我的评测层：其AutoGEEval-Bench的单元级测试用例（函数调用→执行验证）思路可迁移为我的L3规划与L3→QGIS landing评测设计；其多维度指标（准确率/资源/效率/错误类型）可借鉴为我的三层评测与错误分类标准；18个LLM的横向结果可作为M2/M3路线（领域SFT、QLoRA微调）在GEE平台上的可对比基线与data资源，也支撑'NL2Code+平台自动化'动机论证。

### ⭐⭐⭐⭐ GIScience in the Era of Artificial Intelligence: A Research Agenda Towards Autonomous GIS
**8/10** · Zhenlong Li、Huan Ning、Song Gao、Krzysztof Janowicz、Wenwen Li、Samantha T. Arundel · arXiv · 2025-03-31 · [原文](https://arxiv.org/abs/2503.23633v5)
*来源：强命中*

**一句话**：提出自主GIS的概念框架（五个目标、五级自主、五项核心功能、三个尺度），并用四个概念验证智能体展示LLM驱动的地理数据检索、空间分析与制图。

痛点：传统GIS空间分析依赖人工编排地理处理工作流，生成式AI与LLM为地理信息表示、计算和知识生产提供了新范式。方法：以LLM作为决策核心，定义自主GIS并展示GIS agents自动生成与执行地理处理工作流的概念验证。结果：给出自主GIS愿景、关键挑战与未来方向，包括决策核心微调/自生长、自主建模及社会影响。

> 🔗 **与课题**：与课题高度相关，提供自主GIS和LLM决策核心的总体验证框架。其自动生成并执行地理处理工作流对应我的L3规划与L3→QGIS landing目标；五个自主等级/核心功能可作为工作流构建能力分级与评测维度；微调/自生长决策核心呼应M2领域继续预训练、SFT和M3 QLoRA；但未涉及QGIS算子链、统一IR、知识图谱约束解码或具体可复现方法，因此主要作为背景框架与概念基线。

### ⭐⭐⭐⭐ GeoTool-GPT: a trainable method for facilitating Large Language Models to master GIS tools
**8/10** · Wei Cheng、Yifan Zhang、Xinru Zhao、Ziyi Zeng、Zhiyun Wang、Jianfeng Lin · International Journal of Geographical Information Systems · 2024-12-11 · [原文](https://doi.org/10.1080/13658816.2024.2438937)
*来源：强命中*

**一句话**：作者构建了GIS工具理解指令集GeoTool(1950条)、工具链方案数据GeoSolution(3645条)与评测集GeoTask(300条)，并基于LLaMA-2-7b微调出GeoTool-GPT，使通用LLM掌握GIS工具调用并能为地理空间任务生成多工具组合方案。

痛点在于通用LLM缺乏GIS领域语料，既不懂专业GIS工具功能，也难以组合多个工具完成复杂地理空间任务，且缺少领域工具调用评测基准。方法上以自建指令-回答、指令-方案、指令-方案评测三类数据，对LLaMA-2-7b做领域微调得到GeoTool-GPT。实验表明该训练方法显著提升了通用LLM在专业GIS领域的工具使用与方案生成能力。

> 🔗 **与课题**：直接对应M2/M3路线：提供了GIS工具调用领域的指令数据构建范式与SFT微调基线，可对比其LLaMA-2-7b微调效果与我的Qwen3.5-9B DAPT+SFT方案；GeoTask评测集可作为工具使用能力的参考基准（与我的L3规划/L3→QGIS landing评测可比对）；其'指令-方案'多工具组合数据也对应我的工作流算子链构建任务与过程监督数据来源。

### ⭐⭐⭐⭐ Chain-of-Programming (CoP) : Empowering Large Language Models for Geospatial Code Generation
**8/10** · Shuyang Hou、Haoyue Jiao、Zhangxiao Shen、Jianyuan Liang、Anqi Zhao、Xiaopu Zhang · arXiv · 2024-11-16 · [原文](https://arxiv.org/abs/2411.10753v1)
*来源：强命中*

**一句话**：提出Chain-of-Programming (CoP)框架，将地理空间代码生成拆解为需求分析、算法设计、代码实现、调试与注释五步，并融合共享信息池、知识库检索和用户反馈，实现无需微调的端到端生成。

痛点在于用户需求不完整/不清晰以及LLM缺乏特定平台语法知识，导致生成不可执行代码的“代码幻觉”。方法上，CoP把生成流程分解为五个阶段，引入共享信息池、知识库检索与用户反馈机制，并基于地理空间问题分类框架和评测基准进行验证。结果显示生成代码的逻辑清晰性、语法正确性和可执行性提升3.0%至48.8%，消融实验和案例研究进一步验证了关键组件的合理性与必要性。

> 🔗 **与课题**：与课题的landing、eval、baseline模块高度相关：该工作面向地理空间代码生成（GIS平台代码），提出免微调的多阶段提示/检索增强流程，可作为M2领域继续预训练与M3 QLoRA微调路线的重要对比基线；其需求分析→算法设计→代码实现→调试的分阶段结构，与我的QGIS工作流自动构建及分级回退修复思路相近；知识库检索对应RAG/KG增强生成；其地理空间问题分类框架与评测基准可借鉴用于L3→QGIS landing和最终工作流人工可用率评测设计。

### ⭐⭐⭐⭐ Automating Geospatial Analysis Workflows Using ChatGPT-4
**8/10** · Qianheng Zhang、Song Gao · 预印本 · 2024-10-29 · [原文](https://doi.org/10.1145/3678717.3695760)
*来源：作者跟踪: Song Gao*

**一句话**：该研究测试用提示工程驱动 ChatGPT-4 依据结构化指令生成 ArcPy 函数，以自动化 ArcGIS Pro 地理处理工作流，任务成功率约 80.5%。

痛点是非专家用户难以用 Python 脚本自动化 ArcGIS Pro 等 GIS 地理处理流程。方法上，作者用结构化提示与提示工程让 ChatGPT-4 理解空间数据和 GIS 工作流并生成 ArcPy 代码。结果显示整体任务成功率 80.5%，表明该方式对领域科学家可行且易落地。

> 🔗 **与课题**：直接相关于 NL2GIS 工作流自动构建与 L3→平台 landing 问题，可作为 M3（官方后训练模型 QLoRA/提示基线）在 GIS 算子链生成上的可对比基线；其 ArcGIS/ArcPy 落地经验可迁移到 QGIS 算子树映射与最终工作流可用率评测，并为评测任务设计提供参考。

### ⭐⭐⭐⭐ ChatGPT for Intelligent Spatial Analysis Workflow Construction
**8/10** · Ying Nie、Song Gao · 预印本 · 2024-10-29 · [原文](https://doi.org/10.1145/3678717.3695759)
*来源：作者跟踪: Song Gao*

**一句话**：该预印本研究用ChatGPT通过提示工程自动生成基于ArcGIS地理处理工具的空间分析工作流，并探索地理知识与结构化提示对生成效果的改进。

痛点是用AI构建可执行、集成数据模型与领域知识的科学工作流能力仍很有限；方法上以ChatGPT聊天机器人为核心，通过提示工程、引入地理知识(geo-knowledge)与结构化提示来生成ArcGIS空间分析工作流；初步结果表明这些策略提升了ChatGPT生成GIS工作流的准确性与有效性。

> 🔗 **与课题**：与课题高度相关：直接对应"自然语言任务描述→GIS地理处理工具链自动构建"，可作为M3(官方后训练模型)及纯prompt零样本基线的直接对比对象；其landing目标是ArcGIS而非QGIS，但工具映射/工作流落地方法论可迁移到L3→QGIS landing模块；其提出的geo-knowledge与结构化提示思路与KG约束解码、知识增强生成(KG/RAG)路线相关，其识别的挑战(顺序正确性、可解释性、工具选择)对应我们的L3规划与评测维度。

### ⭐⭐⭐⭐ An LLM Agent for Automatic Geospatial Data Analysis
**8/10** · Yuxing Chen、Weijie Wang、Sylvain Lobry、Camille Kurtz · arXiv (Cornell University) · 2024-10-24 · [原文](https://doi.org/10.48550/arxiv.2410.18792)
*来源：强命中*

**一句话**：提出 GeoAgent 交互式框架，用代码解释器、静态分析、RAG 与蒙特卡洛树搜索(MCTS)协同驱动 LLM 完成地理空间数据处理，并配套发布单轮/多轮地理空间代码生成基准。

痛点：LLM 在复杂顺序化的地理空间数据处理任务中易产生逻辑错误，难以融合复杂数据结构与空间约束、调用多样函数并易幻觉不常用地学库。方法：GeoAgent 将代码解释器、静态分析与 RAG 嵌入 MCTS 搜索，实现多步代码生成与自我修正，同时贡献覆盖数据获取/分析/可视化的单轮与多轮评测基准。结果：实验表明仅靠 LLM 内隐知识不足以完成准确的地理空间编程，需要连贯的多步流程与多次函数调用。

> 🔗 **与课题**：高度相关。(1) 任务设定与我的课题一致：自然语言→地理空间处理代码/算子序列的自动生成；(2) 其 RAG + 静态分析 + 搜索式自我修复的组合，可与我的 KG 约束解码+分级回退修复对照，作为 M1 符号约束路线的对比方案；(3) 其多轮、多库、多步流程评测基准，可直接作为我‘L3→QGIS landing/最终工作流可用率’评测的参考或补充数据源，并作为 M2/M3 (Qwen3.5 微调、QLoRA 基线) 的可比基线；(4) 但其面向 Python 生态而非 QGIS 地理处理工作流，缺少显式操作原语 IR 与顺序合法性约束，正是我 L3 中间表示与转移合法性矩阵要弥补的空白。

### ⭐⭐⭐⭐ Evaluation of Code LLMs on Geospatial Code Generation
**8/10** · Piotr Gramacki、Bruno Martins、Piotr Szymański · arXiv · 2024-10-06 · [原文](https://arxiv.org/abs/2410.04617v2)
*来源：强命中*

**一句话**：构建了一个面向地理空间代码生成的评测基准，按任务复杂度与所需工具分类，人工编写题目并配套可自动判定正确性的测试场景，并评测了若干现有代码生成LLM。

痛点：代码生成LLM在地理空间领域面临不同挑战，却通常缺乏针对性评测，难以衡量其空间推理与GIS工具使用能力。方法：作者按复杂度与所需工具对地理空间任务分类，人工构建包含空间推理、空间数据处理、地理工具调用等题目的数据集，并为每题设计可自动校验生成代码正确性的测试场景，随后评测了一批现有代码生成LLM。结果：公开了数据集与可复现评测代码，可作为后续LLM在地理空间代码生成上的评测基准。

> 🔗 **与课题**：直接对应我课题的评测层：可作为L3→QGIS landing与最终代码可用率的评测基准/数据来源，并提供现有代码LLM在GIS代码生成上的可对比基线（对照M1/M2/M3三条路线的落地效果）。差异在于其粒度是单段地理空间代码的生成与单元测试校验，而非完整、顺序正确、可解释的QGIS地理处理工作流（算子链）构建，也不涉及IR、KG约束解码或过程监督，因此可作为任务级下游评测集与基线，而非规划层方法借鉴。

### ⭐⭐⭐⭐ ChatGeoAI: Enabling Geospatial Analysis for Public through Natural Language, with Large Language Models
**8/10** · Ali Mansourian、Rachid Oucheikh · ISPRS International Journal of Geo-Information · 2024-10-01 · [原文](https://doi.org/10.3390/ijgi13100348)
*来源：强命中*

**一句话**：基于 Llama 2 构建 ChatGeoAI 框架，通过实体识别、地理本体映射与代码生成模块，将自然语言查询转换为可执行的 PyQGIS 脚本。

痛点是非专业用户难以用 GIS 进行地理空间分析，需要跨越自然语言意图与 QGIS 编程之间的鸿沟。方法上以 Llama 2 为核心，结合定制实体识别、地理本体映射与语义增强，把用户意图解析为 GIS 操作并生成 PyQGIS 代码执行与可视化。结果在递增复杂度的多类地理空间任务（几何、空间关系、属性查询）上验证了系统的可用性与准确性。

> 🔗 **与课题**：直接对应课题的 landing（L3→QGIS）环节，展示了 NL→PyQGIS 脚本的端到端落地路径；其本体映射机制可对照 KG 约束解码与 I/O 类型约束；递增复杂度的任务测试可借鉴为 L3→QGIS landing 与人工可用率的评测设计；作为 NL2GIS 工作流的可对比基线，与 M2（领域继续预训练+SFT）和 M3（QLoRA 微调）路线属同类方法但未涉及工作流顺序/IR/修复机制。

### ⭐⭐⭐⭐ GeoGPT: An assistant for understanding and processing geospatial tasks
**8/10** · Yifan Zhang、Wei Cheng、Zhengting He、Wenhao Yu · International Journal of Applied Earth Observation and Geoinformation · 2024-06-17 · [原文](https://doi.org/10.1016/j.jag.2024.103976)
*来源：强命中*

**一句话**：提出 GeoGPT 框架，用 LLM 理解自然语言地理任务需求并自主推理、顺序调用 GIS 工具完成数据采集、处理与分析。

痛点在于 GIS 决策者需手工组合多种空间算法与操作，任务稍有差异就要调整工作流，效率低。方法上借鉴 AutoGPT 思路，把 LLM 的语义理解与推理能力同 GIS 领域成熟工具结合，让模型自主思考、规划并顺序执行预定义 GIS 工具，直接以自然语言指令为输入。结果通过系统性评估和地理数据爬取、空间查询、设施选址、制图等案例验证了框架的有效性与通用性。

> 🔗 **与课题**：高度相关于课题的 L3 算子链自动构建与 L3→QGIS landing：其“LLM 规划+顺序调用 GIS 工具”正是可对比的 baseline（属 M3 官方模型任务级/agent 路线），其任务类型（空间查询、选址、制图）可作为我的评测基准用例来源；但其工具调用是无约束的 ReAct/AutoGPT 式推理，缺少 L3 中间表示、I/O 类型与转移合法性约束、KG 约束解码与回退修复机制，可用于论证 M1/M2 在顺序正确性与可解释性上的改进空间。

## 👀 6-7 分：值得一看（29 篇）

### ⭐⭐⭐⭐ VisCritic-GIS: A Visualization-Critic–Empowered Framework for Multi-Agent Geospatial Task Reasoning and Execution
**7/10** · Qing Lan、Linshu Hu、Sensen Wu、Zhenhong Du · 预印本 · 2026-03-14 · [原文](https://doi.org/10.5194/egusphere-egu26-10473)
*来源：领域×任务*

**一句话**：提出 VisCritic-GIS 多智能体框架，在 GIS 智能体中引入可视化生成与多模态批判智能体，用地图证据校验并迭代修正空间推理与工具链配置。

痛点：现有多智能体 GIS 系统多以纯文本 LLM 为推理底座，缺乏显式几何约束与可验证证据，导致拓扑/方向/距离关系推断不一致，并在多步工具调用中误差累积。方法：增加 Visualization Generation Agent 把关键空间数据和中间结果渲染成 2D 地图，再由 Visualization Critic Agent 用多模态 LLM 审阅地图证据，输出关于空间关系、异常结果与推理偏差的文本反馈，反向约束并驱动其他智能体的推理轨迹与工具链配置迭代精化。结果：在代表性地理空间任务上建立了评测协议，验证可视化批判机制可提升任务推理与执行的准确性和效率。

> 🔗 **与课题**：属于 GIS agent/copilot 与 workflow 自动构建方向的可比工作：其“工具链配置 + 多步调用误差累积”问题与我的 M2/M3（LLM 智能体式算子链生成）和 landing 阶段（L3→QGIS 落地失败/回退修复）直接对应；其“可视化证据审查 + 迭代精化”机制可作为我‘分级回退修复’与结果自校验（landing 可用率评估）的对照方案；其多智能体评测协议对 eval 模块（三层评估中的任务级可用率）有参考价值，但不涉及 IR、KG 约束解码或 NL→工作流的形式化生成。

### ⭐⭐⭐⭐ GeoAgent: a hierarchical LLM-based multi-agent architecture for autonomous spatial analysis
**7/10** · Qingming Lin、Liuchang Xu、Sensen Wu、Ruichen Mao、Chao Wang、Hailin Feng · International Journal of Geographical Information Systems · 2026-02-16 · [原文](https://doi.org/10.1080/13658816.2026.2624784)
*来源：强命中*

**一句话**：提出 GeoAgent——规划层/执行层/审查层三层级 LLM 多智能体协作框架，配合三套工具集自主完成空间分析任务。

痛点：复杂空间分析的自主化需要多智能体协作架构，而传统 GIS 在灵活性与动态适应性上存在局限。方法：GeoAgent 采用分层架构——规划层解析需求并生成执行计划，执行层由 manager agent 调度执行代理，审查层实现自主校验与优化，并集成三套环境感知与数据洞察工具集。结果：在 147 个空间分析任务上，GPT-4o 与 DeepSeek-V3 配置分别达到 94.56% 与 95.24% 成功率，消融实验证实规划层与审查层对复杂任务的工作流完整性与结果可靠性起关键作用。

> 🔗 **与课题**：与课题的 L3 规划层、L3→QGIS landing 及评测模块高度相关：其“规划—执行—审查”分层可与我的 L3 原语规划 + 分级回退修复机制对应，Review 层自验证思路可借鉴到修复策略；该框架用官方后训练模型 + 多智能体提示构建，是 M3 路线（官方后训练模型微调基线）的直接可对比基线；其 147 任务评测集可作为 eval 数据参考。但工作停留在工具调用/任务级编排，未涉及平台无关 IR、KG 约束解码或 QGIS 算子级顺序与 I/O 类型约束落地。

### ⭐⭐⭐⭐ Geospatial reasoning and awareness in large language models: a systematic review
**7/10** · Gabriel Ionut Dorobantu、Ana Cornelia Badea · Artificial Intelligence Review · 2026-02-11 · [原文](https://doi.org/10.1007/s10462-026-11512-x)
*来源：强命中*

**一句话**：用PRISMA方法系统综述了大语言模型在地理空间领域的推理与意识能力，涵盖理论、应用、开源/商业模型对比与未来方向。

痛点在于GeoAI领域缺乏对LLM地理空间能力与局限的系统梳理，商业模型虽能理解地理概念并生成可用代码但受限于可及性、透明度与外部基础设施依赖。方法上采用PRISMA规范的系统综述，评估基础模型在地理空间场景中的表现，并比较微调与RAG等适配路径下的小型开源模型。结果指出开源模型在精度、效率和定制性上可作可行替代，但大规模标准化数据集缺失，地理空间智能体在复杂任务中的完全自主仍是未解难题。

> 🔗 **与课题**：与课题高度相关：综述明确了NL2Code/GIS code generation的现状与瓶颈（数据集、评测标准缺失、agent自主性不足），可直接支撑选题动机与related work；其中对fine-tuning与RAG适配开源模型的讨论对应M2领域预训练/指令微调与M3微调基线路线，对标准化评测基准的呼吁对应你的三层评估设计（尤其landing与人工可用率），商业模型代码生成能力对比可作为baseline参考。

### ⭐⭐⭐⭐ A Comprehensive Survey of Agentic AI for Spatio-Temporal Data
**7/10** · Mohammad Hashemi、Andreas Züfle · Preprints.org · 2026-01-28 · [原文](https://doi.org/10.20944/preprints202601.2236.v1)
*来源：领域×任务*

**一句话**：一篇面向时空数据的智能体AI综述，提出涵盖时空数据模态、智能体核心能力与应用场景的统一分类体系，并整理了论文清单。

痛点：时空领域需要智能体整合异构模态、在时空约束下推理，并可靠调用GIS库、地图服务与遥感管线等外部工具，但缺乏系统性梳理。方法：综述LLM驱动的智能体AI在时空智能中的进展，构建“数据模态—智能体能力—应用场景（地理分析、遥感、城市规划、 mobility）”三维统一分类法，并提供GitHub论文列表。结果：形成该交叉领域的路线图与资源索引，指出工具调用与时空约束下的可靠性是关键开放问题。

> 🔗 **与课题**：直接对应课题的GIS agent/copilot与工具调用（tool-mediated actions、GIS libraries/map services/Earth observation pipelines）方向，可作为相关工作与选题定位的综述引用；其分类法可用于组织M1/M2/M3的评测维度与任务类型，并辅助landing层的算子—工具映射设计，但本身不提供模型或可对比基线。

### ⭐⭐⭐⭐ On the Use of LLMs for GIS-Based Spatial Analysis
**7/10** · Roberto Pierdicca、Nikhil Muralikrishna、F. Tonetto、Alessandro Ghianda · ISPRS International Journal of Geo-Information · 2025-10-14 · [原文](https://doi.org/10.3390/ijgi14100401)
*来源：领域×任务*

**一句话**：用 GPT-4 与 DeepSeek-R1 把自然语言指令转成 Python 脚本来自动执行 GIS 空间分析任务，并与 10 名 GIS 分析师的手工流程对比。

痛点在于 GIS 空间分析门槛高、依赖专业技能且手工操作耗时。作者构建了一个 LLM 驱动的系统（配 CustomTkinter GUI），将用户自然语言指令翻译为动态生成的 Python 脚本以完成空间数据校验、合并、缓冲区分析和专题制图等任务，并在意大利 Pesaro 城市数据上做了对比案例研究。结果显示任务完成时间从手工约 1 小时 45 分降至约 27 分钟，且分析质量与精度未受损，另外还通过多样地理查询评估了系统的事实可靠性。

> 🔗 **与课题**：属于同任务的 GIS NL→自动化工作流竞品系统，可作为 M3（官方后训练模型提示/QLoRA）与 landing、eval 层的可对比基线：其'自然语言→可执行 GIS 流程'目标与本课题一致，人工分析师的可用率/耗时对比方法可直接借鉴到最终工作流人工可用率评测；但其输出是自由生成的 Python 脚本而非 QGIS 地理处理算子链，既无 L3 操作原语中间表示，也无 KG 约束解码与 I/O 类型校验，可作为'无 IR、无符号约束'的消融式对照，用以论证 M1（KG 约束解码）与 L3 中间表示的必要性。

### ⭐⭐⭐⭐ Generative AI for Geospatial Analysis: Fine-Tuning ChatGPT to Convert Natural Language into Python-Based Geospatial Computations
**7/10** · Zachary Sherman、Sandesh Sharma Dulal、Jin-Hee Cho、Mengxi Zhang、Junghwan Kim · ISPRS International Journal of Geo-Information · 2025-08-18 · [原文](https://doi.org/10.3390/ijgi14080314)
*来源：领域×任务*

**一句话**：该研究用600+条地理空间Python脚本问答对微调GPT-4o-mini，将自然语言查询翻译为可执行的地理空间Python代码，并与未微调基线对比。

痛点是非技术用户难以使用传统GIS工作流，LLM虽提供对话式交互但直接生成地理空间代码的正确率低。方法上以Virginia地区US Census shapefile与医院数据为场景，构建600+提示-响应对微调GPT-4o-mini，并引入空间推理、模块化外部函数调用与模糊地名纠错。结果微调模型在六类空间查询上准确率从基线40.5%提升至89.7%（+49.2个百分点），同时显著减少执行错误与token消耗。

> 🔗 **与课题**：与课题高度相关：属于NL2Code/地理空间代码生成方向，是M3路线（官方后训练模型任务级微调）的直接可对比基线与数据来源参考——其600+ prompt-response对可类比你的领域指令SFT数据构建；评估用执行成功率、执行错误数、token消耗，可借鉴到你的三层评估中L3→落地与人工可用率指标；其模块化外部函数调用、模糊地理输入纠错思路也可迁移到landing与分级回退修复模块。

### ⭐⭐⭐⭐ A DeBERTa-Based Semantic Conversion Model for Spatiotemporal Questions in Natural Language
**7/10** · Wenjuan Lu、Dongping Ming、Xi Mao、Jizhou Wang、Zhanjie Zhao、Yao Cheng · Applied Sciences · 2025-01-22 · [原文](https://doi.org/10.3390/app15031073)
*来源：领域×任务*

**一句话**：该文提出NL2Cypher模型，基于DeBERTa+BiGRU+CRF对中文自然语言时空问题进行语义抽取与意图识别，并转换为Cypher图查询语句。

痛点在于自然语言时空查询存在语义理解不足、信息抽取不全、意图识别不准的问题。方法上先用DeBERTa编码时空问题并用BiGRU+CRF做序列标注，再据此进行意图分类与语义解析，最终生成Cypher查询。结果显示简单与复合查询下F1达92.69%，问题到查询语言转换准确率训练集88%、测试集92%，优于对比模型。

> 🔗 **与课题**：与课题的KG约束与语义解析模块相关：(1) 其“NL→结构化图查询(Cypher)”范式与M1的转移合法性/I-O类型约束解码思路同源，可作为NL2Cypher式约束生成的对比基线；(2) DeBERTa+BiGRU+CRF的编码-标注结构可为M1的BERT文本编码与意图/槽位识别提供参考或作为初步实验的轻量基线；(3) 其时空问题语料与意图分类体系可为KG增强生成及评测（意图识别/语义解析指标F1）提供数据与评测参考，但不涉及QGIS工作流算子链构建与landing。

### ⭐⭐⭐⭐ BB-GeoGPT: A framework for learning a large language model for geographic information science
**7/10** · Yifan Zhang、Zhiyun Wang、Zhengting He、Jingxuan Li、Gengchen Mai、Jianfeng Lin · Information Processing & Management · 2024-06-22 · [原文](https://doi.org/10.1016/j.ipm.2024.103808)
*来源：作者跟踪: Gengchen Mai*

**一句话**：提出 BB-GeoGPT 框架，用于训练/适配面向地理信息科学领域的大型语言模型。

该工作关注地理信息科学领域缺乏专用大语言模型的问题，提出 BB-GeoGPT 框架进行地理领域 LLM 的学习与适配。由于摘要未提供，其具体数据构建、训练目标和评测结果无法确认；从标题看，方法应涉及地理领域语料/知识注入、模型训练及 GIS 任务评测。整体可作为地理领域大模型基线及相关领域适配研究参考。

> 🔗 **与课题**：与 M2 路线相关：同属地理领域大模型继续预训练/领域指令微调/领域适配方向，可为领域数据构造、SFT 数据、地理知识注入和基线对比提供参考；若其含 GIS 问答或评测基准，也可辅助 M3 任务级 QLoRA 微调与 eval 设计。不直接涉及 QGIS 工作流自动构建、L3 IR、KG 约束解码或 landing。

### ⭐⭐⭐⭐ A flood knowledge-constrained large language model interactable with GIS: enhancing public risk perception of floods
**7/10** · Jun Zhu、Pei Dang、Yungang Cao、Jianbo Lai、Yukun Guo、Ping Wang · International Journal of Geographical Information Systems · 2024-02-06 · [原文](https://doi.org/10.1080/13658816.2024.2306167)
*来源：领域×任务*

**一句话**：提出一种受洪水知识图谱约束、能与GIS交互的大语言模型框架，用于通过自然语言对话增强公众洪水风险感知。

痛点：公众对洪水风险的感知不准确，需要自然语言交互提供准确且易懂的信息。方法：用洪水知识图谱中的实体和关系约束LLM生成，并让LLM与GIS交互，通过实时编码生成个性化知识。结果：LLM在知识约束下能生成准确的洪水信息，用户实验表明自然语言对话可缩小不同认知水平带来的知识获取差异。

> 🔗 **与课题**：与课题相关：涉及知识图谱约束生成（类似KG约束解码）、LLM与GIS交互（landing）、实时编码生成GIS操作（NL2Code），可作为M2领域LLM应用案例或baseline参考；但未涉及QGIS地理处理工作流自动构建，侧重洪水风险感知对话。

### ⭐⭐⭐ Preface to the GeoFM 2026 Workshop Proceedings: Geography According to Foundation Models
**6/10** · Krzysztof Janowicz、Alexandra Fortacz、Yingjing Huang、Rui Zhu、Grant McKenzie · Zenodo (CERN European Organization for Nuclear Research) · 2026-06-13 · [原文](https://doi.org/10.5281/zenodo.20666985)
*来源：作者跟踪: Rui Zhu, Krzysztof Janowicz(碎片), Grant McKenzie*

**一句话**：这是 GeoFM 2026 研讨会论文集的索引卷，汇总了各篇贡献论文，其中包括自然语言到地理空间代码生成基准 Bench4GeoCode。

该文献本身是会议论文集前言/索引，不提出新方法，只列出研讨会接收论文及 DOI。其中收录了 Bench4GeoCode：一个面向自然语言到地理空间代码生成的基准，与 QGIS/GEE 自动化工作流评测高度相关。整体价值主要在于发现可参考的评测基准和相关社区工作，而非直接技术方案。

> 🔗 **与课题**：与评测模块直接相关：Bench4GeoCode 可作为 L3 规划、L3→QGIS landing、最终工作流可用率评估的可对比基准；同时涉及 GIS 基础模型与 NL2Geospatial Code 方向，可作为数据/基线线索。

### ⭐⭐⭐ Towards Intelligent Geospatial Data Discovery: a knowledge graph-driven multi-agent framework powered by large language models
**6/10** · Ruixiang Liu、Zhenlong Li、Ali Khosravi Kazazi · arXiv (Cornell University) · 2026-03-21 · [原文](https://openalex.org/W7140953654)
*来源：作者跟踪: Zhenlong Li*

**一句话**：该论文提出一个由大语言模型驱动的知识图谱多智能体框架，用统一地理元数据本体作为语义中介层构建地理元数据知识图谱，并通过意图解析—图谱检索—答案合成的多智能体协作实现可解释的地理数据发现。

痛点：地理数据生态分布异构、语义不一致，传统目录与门户仅靠关键词检索，难以捕捉用户意图、召回与排序质量差。方法：定义统一地理元数据本体作为跨平台元数据标准的语义中介层，构建显式建模数据集及多维关系的地理元数据知识图谱，再以多智能体架构完成意图解析、KG 检索与答案合成，形成可解释的闭环发现流程。结果：代表性用例与性能评估显示其在意图匹配准确率、排序质量、召回率与发现透明度上均优于传统系统。

> 🔗 **与课题**：与课题在"KG 增强 + LLM 智能体 + 语义中介层"三点上直接呼应：(1) 其"统一地理元数据本体/语义中介层"与我的 L3 平台无关操作原语 IR 思路同构，都是把异构 GIS 平台语义对齐到统一中间层，可作为 L3 设计的类比依据与相关工作引用；(2) 其 KG 检索增强智能体的做法可对照我的 M1 知识图谱约束解码（转移合法性、I/O 类型约束）与分级回退修复，说明 KG 在 GIS 领域如何被结构化用于约束生成；(3) 其"意图解析→检索→合成"的多智能体闭环可作为 M2（Qwen3.5 领域 DAPT+SFT）与 M3（官方后训练模型 QLoRA）agent 化路线的对比基线或架构参考；(4) 论文评测指标（意图匹配准确率、排序质量、召回率、透明度）对我在 L3 规划层与最终工作流人工可用率的评测设计有借鉴价值。差异在于该文面向"数据发现/检索"而非"工作流（算子链）自动构建与 landing 到 QGIS"，因此不涉及算子顺序正确性、可执行落地与过程监督，属于弱相关偏 KG/评测参考。

### ⭐⭐⭐ A controlled natural language and interface for formulating geo-analytical questions with Blockly
**6/10** · Haiqi Xu、Enkhbold Nyamsuren、Eric J. Top、Simon Scheider · International Journal of Geographical Information Systems · 2026-03-03 · [原文](https://doi.org/10.1080/13658816.2026.2635476)
*来源：强命中*

**一句话**：提出一套受控自然语言加地理分析概念变换语义模型，并在定制 Blockly 界面中让用户像搭积木一样组装地理分析问题，以提升问题的标准化与可解释性。

痛点：面向地理处理工作流生成的地理分析问答系统，其输出质量高度依赖输入问题是否足够清晰、完整和可解释，而自由形式提问往往做不到。方法：作者将受控自然语言（表达地理分析意图）与一个地理分析概念变换的语义模型结合，实现为定制的 Google Blockly 界面，用户通过选择并连接代表问题概念组件的块来构造问题。结果：用户实验显示 Blockly 界面能有效约束提问，产生更标准化、完整、可解释的问题且不受用户 GIS 专业水平影响，但学习成本更高、可用性评分中低；作者建议未来将该受控语言与生成模型结合以提升质量与可扩展性。

> 🔗 **与课题**：与 L3 与评测/landing 环节相关：其“地理分析概念变换的语义模型”在思想上与我 L3 平台无关操作原语/统一语义层高度类似，可作为 NL 问句到 L3 IR 的形式化前端与约束来源；受控语言产出的标准化问题可当作评测题集与输入规范，直接服务于“L3→QGIS landing”和最终工作流人工可用率评估，并提高输入可解释性。但该工作不涉及模型训练、自回归解码、KG 约束解码或工具调用链自动生成，故不能作为 M1/M2/M3 的方法基线，只能作为问题形式化与评测数据侧的参考。

### ⭐⭐⭐ GNLM: A Graph-Native Language Model With Road Name Address-Based Spatial Reasoning for Geographic Question Answering
**6/10** · Chae-Seok Lee、Dae-seung Park、Jae-min Choi、Ho-jong Chang · IEEE Access · 2026-01-01 · [原文](https://doi.org/10.1109/access.2026.3695549)
*来源：强命中*

**一句话**：提出 GNLM（图原生语言模型），把地理问答的全部推理交给知识图谱遍历（基于路名地址与建筑登记公共数据构建 RDF 三元组），LLM 仅负责自然语言生成。

痛点：现有基于 LLM 的地理问答存在事实幻觉，而 RAG 缺乏结构化推理能力。方法：构建 Graph-First/LLM-Last 架构，用扩展 RDF 三元组属性模型把实体属性建模为独立图节点，支持无坐标的空间邻近排序（韩国路名编号标准）与 14 策略推理路由器，知识全部来自政府公开数据与专家知识。结果：结构性避免伪造，所有观测错误均来自知识缺口而非虚假生成，提升地理问答的事实可靠性与属性级/元推理能力。

> 🔗 **与课题**：与课题的 KG 相关：可作为 M1 路线中"知识图谱增强/约束生成"的对照思路——它把 KG 放在推理主路径、LLM 只做表层生成，与我的"IR + 转移合法性矩阵约束解码、I/O 类型约束、分级回退"形成可比较的 neuro-symbolic 设计取舍；其 RDF 属性级查询、空间关系（邻近排序）语义建模可借鉴到 L3 操作原语的 I/O 类型与空间谓词体系；同时可参考其地理问答评测方式（事实可靠性/错误归因分析）用于我的三层评测中的 L3 规划层。但该工作不涉及工作流/算子链构建、GIS 软件 landing 或工具调用，也不是 NL2Code。

### ⭐⭐⭐ Predictive GIS Modelling for Renewable Energy Site Suitability Using LLM Reasoning Pipelines
**6/10** · Dhruv Dawar、Shivya Khandpur、Sneha Roychowdhury、Arun Sharma、Deeptanshu Jha · 预印本 · 2025-11-27 · [原文](https://doi.org/10.1109/aist68591.2025.11441593)
*来源：领域×任务*

**一句话**：提出 GeoSolarX 混合 AI-GIS 框架，用模板引导的 LLM 思维链规划器加确定性 GIS 算子，把自然语言选址需求落地为可再生能源选址分析。

痛点：传统 GIS 工作流僵化、依赖专家技术能力，且可再生能源选址受监管与环境约束、涉及多类数据和多利益相关方。方法：构建带对话界面的混合 AI-GIS 架构，用固定融合权重的多模态加权融合（影像、表格属性、文本、时序、图结构）配合模板引导的 Chain-of-Thought 规划器与确定性地理处理操作，并提供多语言语音接口。结果：面向政策制定者、规划者与农村用户提供无需 GIS 专业知识的可解释空间决策支持（预印本，摘要未给出量化评估结果）。

> 🔗 **与课题**：与我的课题在"自然语言任务描述→地理处理算子链 landing"这一环节高度相关：其模板引导 CoT 规划器+确定性 GIS 操作可类比我的 L3 操作原语与 M1/M2 的规划解码与落地执行，可解释性诉求对应我的三层评估中的 landing 与人工可用率；差异在于它依赖固定权重多模态融合而非知识图谱约束解码/转移合法性矩阵，QGIS 算子级映射与顺序正确性验证也非其重点。可作为 GIS copilot/agent 方向的相关工作与 landing 阶段的对比基线，并可作为领域数据/场景（选址类任务）参考。

### ⭐⭐⭐ Intelligent National Map: A Vision for Distributed and Agentic Geospatial Intelligence
**6/10** · Samantha T. Arundel、Wenwen Li、Kevin McKeehan、B. B. Campbell、Jung‐Kuan Liu、Lawrence V. Stanislawski · 预印本 · 2025-08-28 · [原文](https://doi.org/10.31223/x5w163)
*来源：作者跟踪: Wenwen Li*

**一句话**：提出“智能国家地图”(INM)愿景，用多智能体编排、自然语言接口与RAG实现自主协调的地理空间分析工作流。

痛点：现有国家测绘机构的数据服务是静态的，用户难以自主完成复杂的空间分析并获取可信答案。方法：论文给出INM的概念与技术基础，以多智能体编排、自然语言交互、检索增强生成(RAG)和对可信公共数据的访问为核心，由用户输入触发任务专属agent去定位、分析并解释结果，强调语义关系、领域规则与已验证工作流支撑的结构化推理，并具备自审、自纠与持续学习能力。结果：属于愿景/立场性预印本，未给出具体系统实现或量化评测。

> 🔗 **与课题**：与课题高度同源但偏概念层：其“natural language interfaces + task-specific agents + validated workflows + RAG + 语义关系/领域规则约束推理”对应我的NL2工作流自动构建、L3操作原语IR与KG约束解码、以及自审自纠可类比我的分级回退修复机制；可作为GIS agent/copilot方向的背景与动机引用。但该文无实现、无数据集、无基准，不能作为M1/M2/M3的可对比基线，也未涉及QGIS落地(landing)。

### ⭐⭐⭐ CityGPT: Empowering Urban Spatial Cognition of Large Language Models
**6/10** · Jie Feng、T. Liu、Yangzhou Du、Siqi Guo、Yuming Lin、Yong Li · 预印本 · 2025-08-01 · [原文](https://doi.org/10.1145/3711896.3736878)
*来源：领域×任务*

**一句话**：构建城市空间知识指令数据集 CityInstruction、自加权微调方法 SWFT 与文本化城市空间评测基准 CityEval，用于增强 LLM 的城市空间认知与地理推理能力。

痛点：LLM 在真实城市地理空间任务上表现不佳，因为训练中缺乏物理世界知识与相关数据。方法：作者提出 CityGPT 框架，构建城市级“世界模型”，发布 CityInstruction 指令微调数据集，并提出自加权微调方法 SWFT，将城市指令与通用指令混合训练 ChatGLM3-6B、Llama3-8B、Qwen2.5-7B 等模型。结果：同时发布文本化空间评测基准 CityEval，实验表明经 SWFT 训练的小模型在城市空间任务上取得显著提升且不损害通用能力。

> 🔗 **与课题**：与 M2 路线高度相关：其 CityInstruction 领域指令数据构建与 SWFT 混合微调策略可迁移到 QGIS/地理处理领域的 DAPT+SFT 流程；CityEval 提供了可借鉴的文本化地理任务评测基准设计思路（对应我的评测层）；但其任务是城市空间问答/推理而非 NL2Code 或工作流构建，不涉及 IR、KG 约束解码、算子链 landing，因此可作为 M2 领域微调与评测设计的数据/基线参考，而非直接竞品。

### ⭐⭐⭐ GeoJSEval: An Automated Evaluation Framework for Large Language Models on JavaScript-Based Geospatial Computation and Visualization Code Generation
**6/10** · Guanyu Chen、Haoyue Jiao、Shuyang Hou、Ziqi Liu、Lutong Xie、Shaowen Wu · arXiv · 2025-07-28 · [原文](https://arxiv.org/abs/2507.20553v1)
*来源：强命中*

**一句话**：提出 GeoJSEval——首个面向 JavaScript 地理空间计算与可视化代码生成的多模态、函数级自动评测框架，含 432 个任务、2071 条测试用例并评测 18 个主流 LLM。

痛点：LLM 地理空间代码生成缺乏系统化评测手段，而 JS 环境下需协调多种前端地理库与数据类型，对语义理解与代码合成要求高。方法：构建 GeoJSEval-Bench 标准测试集、代码提交引擎与评测模块，覆盖 5 个 JS 地理库、25 类地理数据，从准确率、输出稳定性、执行效率、资源消耗、错误类型分布等维度量化评估，并引入边界测试。结果：对 18 个 SOTA LLM 的评测揭示了显著性能差异与瓶颈。

> 🔗 **与课题**：主要支撑我课题的评测层：可作为 L3→landing 与最终生成结果评测方法论的参照（函数级、可执行、多维度指标、错误类型分布、边界测试设计），其 benchmark 构建思路与任务/测试用例组织方式可迁移到 QGIS 工作流评测（eval 模块、数据构建）；同时其评测结论可作为 GIS code generation 领域基线参考，但针对的是单函数 JS 代码而非顺序化算子链工作流，不涉及 IR、KG 约束解码或 DPO 训练。

### ⭐⭐⭐ Foundation models for geospatial reasoning: assessing the capabilities of large language models in understanding geometries and topological spatial relations
**6/10** · Yuhan Ji、Song Gao、Ying Nie、Ivan Majić、Krzysztof Janowicz · International Journal of Geographical Information Systems · 2025-06-02 · [原文](https://doi.org/10.1080/13658816.2025.2511227)
*来源：作者跟踪: Song Gao, Krzysztof Janowicz*

**一句话**：该论文系统评测了 GPT-3.5-turbo、GPT-4、DeepSeek-R1-14B 等大模型在 WKT 几何表示与拓扑空间关系推理上的能力，比较了嵌入、提示工程与日常语言三种策略。

痛点在于预训练基础模型难以直接用于地理空间数据，尤其是对矢量几何与复杂空间关系的表示和推理能力不足。方法上以 WKT 编码几何与拓扑谓词，设计几何嵌入、提示工程、日常语言三类评测流程，对多个 LLM 进行空间关系推理问答测试。结果显示 GPT 系列平均拓扑关系识别准确率可超 0.6，GPT-4 少样本提示最优(>0.66)，并能较好理解逆拓扑关系。

> 🔗 **与课题**：与课题的评测层和 LLM 能力基线相关：其拓扑谓词(WKT、拓扑关系)理解评测可作为 L3 操作原语 I/O 类型/空间谓词约束的先验知识与评测参考，为 KG 约束解码中的空间关系合法性提供语义依据；同时其 prompt/embedding 对比实验可作为 M2/M3 路线在空间语义理解任务上的可对比基线与评测设计借鉴(但未涉及工作流自动构建或算子链生成)。

### ⭐⭐⭐ A question-answering framework for geospatial data retrieval enhanced by a knowledge graph and large language models
**6/10** · Hao Li、Peng Yue、Hui Wu、Baoxin Teng、Yongkun Zhao、Changfeng Liu · International Journal of Digital Earth · 2025-05-26 · [原文](https://doi.org/10.1080/17538947.2025.2510566)
*来源：领域×任务*

**一句话**：该论文提出GDQA系统，用地理空间数据知识图谱(GDKG)结合大语言模型实现自然语言的地理数据检索问答，并提出STRKG方法让LLM在知识图谱上做时空推理。

痛点：地学数据源分散、门户语义支持弱，非专家难以高效检索。方法：先从五大门户抽取构建细粒度地理空间数据知识图谱GDKG，再用STRKG方法让LLM在GDKG上做时空推理与探索，实现自然语言数据发现。结果：在覆盖约束数量、推理深度、时空逻辑、推理复杂度四个维度的能力题集上，相比KGQArr、Text2Cypher、KAPING、ToG等基线在准确率与效率上均更优。

> 🔗 **与课题**：与课题在'KG增强生成'与'地理领域LLM'上相关：(1) 其GDKG构建与STRKG的KG上推理思路，可借鉴到M1路线的知识图谱约束解码/转移合法性约束，以及作为RAG式外部知识支撑；(2) 其四维能力题集(constraint quantity/reasoning depth/spatiotemporal logic/inference complexity)与多基线对比范式，可迁移到课题L3规划层评测设计；(3) 提供地理领域KG与问答数据参考。但该工作面向数据检索QA，不涉及工作流/算子链自动构建与QGIS landing，不能作为直接可对比基线。

### ⭐⭐⭐ Enhancing geodatabases operability: advanced human-computer interaction through RAG and Multi-Agent Systems
**6/10** · Ziming Peng、Xi Kuai、Shuisong Ke、Xuehui Dong、Renzhong Guo · Big Earth Data · 2025-03-30 · [原文](https://doi.org/10.1080/20964471.2025.2483541)
*来源：领域×任务*

**一句话**：该论文提出融合RAG与LLM多智能体系统，将自然语言查询转换为地理数据库SQL查询。

针对地理数据查询效率与准确率问题，利用GIS元数据、RAG外部知识增强和多智能体任务分解，生成语法与语义更准确的SQL。实验在复杂大规模地理数据集上达到80%以上SQL生成准确率，平均执行11.74秒，并在城市规划平台验证了可用性。

> 🔗 **与课题**：与课题在GIS自然语言接口、RAG、多智能体/工具调用和评测上相关；可作为M2/M3路线在GIS领域NL2Code的对比基线或RAG增强参考，但其输出是SQL查询而非QGIS地理处理工作流，未涉及L3操作原语、KG约束解码、landing与工作流顺序正确性。

### ⭐⭐⭐ Context-Aware Visual Prompting: Automating Geospatial Web Dashboards with Large Language Models and Agent Self-Validation for Decision Support
**6/10** · Haowen Xu、Jose Tupayachi、Xiao-Ying Yu · SSRN Electronic Journal · 2025-01-01 · [原文](https://doi.org/10.2139/ssrn.5826382)
*来源：领域×任务*

**一句话**：提出上下文感知视觉提示与智能体自验证方法，用大语言模型自动生成地理空间Web仪表盘以支持决策。

针对地理空间Web仪表盘构建依赖人工、流程复杂的问题，论文提出结合上下文感知视觉提示、LLM与智能体自验证的自动化方法。由于摘要缺失，具体技术细节和实验结果未知；从标题看，面向决策支持场景实现地理空间仪表盘自动生成与校验。

> 🔗 **与课题**：与GIS agent/copilot、NL2Code、工作流自动构建及智能体自验证相关，可作为M3或LLM自动化GIS应用类基线；其self-validation思路可借鉴到landing后工作流可用性校验与分级回退修复，但并非直接面向QGIS地理处理算子链生成。

### ⭐⭐⭐ Mitigating Geospatial Knowledge Hallucination in Large Language Models: Benchmarking and Dynamic Factuality Aligning
**6/10** · Shengyuan Wang、Jie Feng、Tianhui Liu、Dan Pei、Yong Li · 预印本 · 2025-01-01 · [原文](https://doi.org/10.18653/v1/2025.findings-emnlp.45)
*来源：领域×任务*

**一句话**：该论文构建了基于结构化地理知识图谱的地理空间幻觉评测基准，评测了20个LLM，并提出基于KTO的动态事实性对齐方法来缓解地理空间幻觉。

痛点：LLM在地理空间任务中常生成不准确的地理知识（地理幻觉），而该现象的评测与缓解尚缺乏系统研究。方法：利用结构化地理知识图谱做可控评测，构建地理空间幻觉基准，对20个先进LLM进行评测，并提出基于Kahneman-Tversky Optimization (KTO) 的动态事实性对齐训练方法。结果：所提方法在自建基准上性能提升超过29.6%，提升了LLM在地理知识问答与推理任务中的可信度。

> 🔗 **与课题**：与课题部分相关但非核心：其地理知识图谱驱动的幻觉评测思路可作为我"L3规划层事实性/可靠性评测"的参考，KTO偏好对齐属于M2路线（领域偏好后训练）可借鉴的对齐算法（与DPO同类），其开源基准与数据可用于补充地理领域幻觉评测集；但论文不涉及NL2Code、工作流构建、QGIS算子链、IR或约束解码，无法作为规划/landing的直接对比基线。

### ⭐⭐⭐ Large Language Model-Driven Structured Output: A Comprehensive Benchmark and Spatial Data Generation Framework
**6/10** · Diya Li、Yue Zhao、Zhifang Wang、Calvin Jung、Zhe Zhang · ISPRS International Journal of Geo-Information · 2024-11-10 · [原文](https://doi.org/10.3390/ijgi13110405)
*来源：领域×任务*

**一句话**：构建了一个 LLM 生成结构化空间数据（如 GeoJSON）的基准与多步生成框架，并系统比较微调、提示工程与 RAG 三种结构化输出方案。

痛点：LLM 虽能处理文档、代码等任务，但难以生成结构化、统一格式的空间信息，阻碍其进入生产环境。方法：作者提出多步工作流（生成 GeoJSON、R-tree 索引构建）、新数据集与新评测指标，并横向对比 fine-tuning、prompt engineering、RAG 三类使 LLM 输出结构化结果的技术路线。结果：给出了各方法在质量与一致性上的优劣洞察，为从业者选择方案提供依据。

> 🔗 **与课题**：与课题的 eval 与 M2/M3 模块相关：其'结构化空间输出 + 新评测指标/数据集'可为我的 L3→QGIS landing 层与最终工作流可用率评测提供指标设计借鉴；fine-tuning vs RAG vs prompt 的对比结论可佐证 M2 领域 SFT/DAPT 与 M3 QLoRA 路线选择；RAG 部分与我关注的 KG 增强/RAG 相关。但该文聚焦单步结构化空间数据生成而非多算子工作流编排，未涉及 IR、约束解码、KG 转移合法性，故不作核心基线。

### ⭐⭐⭐ Conversational Geographic Question Answering for Route Optimization: An LLM and Continuous Retrieval-Augmented Generation Approach
**6/10** · Jose Tupayachi、Xueping Li · 预印本 · 2024-10-29 · [原文](https://doi.org/10.1145/3681772.3698217)
*来源：强命中*

**一句话**：用连续检索增强生成(Continuous RAG)+微调LLM实现面向路径优化的对话式地理问答，让LLM通过逻辑指令调用GIS API。

痛点在于自然语言地理问答需要结合外部地理数据与API调用能力，纯LLM难以准确检索与执行。方法上采用连续RAG（基于节点的定制存储+向量检索）配合微调LLM，将文本查询映射为API逻辑指令以支持路径优化。结果给出该方法处理多样文本查询的有效性与适应性对比分析，属于试点性质研究。

> 🔗 **与课题**：相关模块：landing（LLM通过逻辑指令调用GIS API，与L3→QGIS算子落地的工具调用思路相通）、RAG（连续检索+节点式向量存储可作为M1/M2知识检索增强的参考）、data/baseline（地理问答任务可作为NL2GIS评测的对比基线）。但未涉及工作流自动化构建、IR中间表示、KG约束解码等核心点。

### ⭐⭐⭐ MapGPT: an autonomous framework for mapping by integrating large language model and cartographic tools
**6/10** · Yifan Zhang、Zhengting He、Jingxuan Li、Jianfeng Lin、Qingfeng Guan、Wenhao Yu · Cartography and Geographic Information Science · 2024-10-03 · [原文](https://doi.org/10.1080/15230406.2024.2404868)
*来源：领域×任务*

**一句话**：提出MapGPT框架，用大语言模型理解自然语言制图需求并按序自动调用多个专业制图工具生成地图，支持对话式调整地图元素。

痛点：制图涉及符号、布局、注记等复杂操作，专业门槛高，而现有深度学习方法把地图当作整体输入输出，无法灵活控制地图内部细节元素。方法：设计多个各控制一类地图元素的专业制图工具，由LLM根据自然语言描述理解需求并依次调用合适工具生成地图，同时用记忆组件存储交互信息以支持对话式修改颜色、位置等元素。结果：实现了用户友好的自动化与可交互制图流程。

> 🔗 **与课题**：与课题中'自然语言→按序调用算子/工具构建工作流'的核心思路直接相关，可作为M2/M3路线（LLM+工具调用/agent）在GIS制图场景的领域对照基线；其'工具按序调用+记忆组件'接近工作流自动构建与landing可行性，但未涉及平台无关IR、KG约束解码、I/O类型约束与QGIS地理处理算子链，评测也仅停留在制图任务而非工作流可用率。

### ⭐⭐⭐ Correctness Comparison of ChatGPT ‐4, Gemini, Claude‐3, and Copilot for Spatial Tasks
**6/10** · Hartwig H. Hochmair、Levente Juhász、Takoda Kemp · Transactions in GIS · 2024-08-12 · [原文](https://doi.org/10.1111/tgis.13233)
*来源：领域×任务*

**一句话**：该论文对 ChatGPT-4、Gemini、Claude-3 和 Copilot 四个聊天机器人在 76 个空间任务（含地图制图、代码编写、空间推理等七类）上做了零样本正确性对比评测。

痛点在于现有 LLM 空间任务性能评估几乎只关注 ChatGPT，缺乏对其他主流聊天机器人的系统比较。方法是对四款聊天机器人分配 76 个覆盖七类的空间任务进行零样本正确性评测，并检验重复提问的响应一致性。结果显示各模型在空间素养、GIS 理论和代码解读上表现较好，但在地图制图、代码编写和空间推理上较弱，且四者正确率存在显著差异，重复任务响应一致率多超过 80%。

> 🔗 **与课题**：与课题的评测层（L3 规划 / L3→QGIS landing / 工作流可用率）直接相关：可作为通用 LLM 在 GIS 空间任务上的外部对比基线与任务类别参考，为构建 NL2GIS 评测基准、衡量 M2/M3 领域适配模型的相对增益提供数据与指标设计借鉴；但其任务为单点问答而非工作流自动构建，未涉及 IR、KG 约束解码或工具链编排。

### ⭐⭐⭐ An Autonomous GIS Agent Framework for Geospatial Data Retrieval
**6/10** · Huan Ning、Zhenlong Li、Temitope Akinboyewa、M. Naser Lessani · arXiv · 2024-07-13 · [原文](https://arxiv.org/abs/2407.21024v2)
*来源：强命中*

**一句话**：提出一个以LLM为决策者、通过生成/执行/调试程序来自动检索地理空间数据的自主GIS智能体框架，并实现为QGIS插件。

痛点是现有LLM驱动的GIS智能体缺乏自主发现并下载分析所需数据的能力，无法端到端自主完成空间分析。方法上用LLM做决策器，从预定义数据源列表中选源，每个数据源配一份记录元数据与技术细节的handbook，智能体据此生成、执行并调试取数程序，框架采用即插即用设计以便扩展新数据源。结果是以QGIS插件（GeoData Retrieve Agent）和Python程序形式发布原型，成功从OSM、美国人口普查局、ESRI World Imagery、OpenTopography DEM、商业天气源、NYTimes COVID-19数据等多源取数。

> 🔗 **与课题**：与课题同属"GIS agent/copilot + LLM工具调用"方向，且是QGIS落地形态，可作为M3/工具调用路线的相关基线与组件参考：(1)其"LLM决策器+数据源handbook"机制本质上是一种轻量工具描述/RAG式工具选择，可对照我的KG约束解码与工具合法性矩阵；(2)其"生成程序—执行—调试"闭环对应我框架中的分级回退修复模块；(3)QGIS插件形态为我的L3→QGIS landing层提供工程实现参考与实际对比对象；(4)局限在于只解决数据获取，不涉及算子链的顺序正确性、I/O类型约束与工作流完整构建，因此与L3规划层相关性较弱，主要在landing/agent工程侧可借鉴。

### ⭐⭐⭐ On the Opportunities and Challenges of Foundation Models for GeoAI (Vision Paper)
**6/10** · Gengchen Mai、Weiming Huang、Jin Sun、Suhang Song、Deepak R. Mishra、Ninghao Liu · ACM Transactions on Spatial Algorithms and Systems · 2024-03-20 · [原文](https://doi.org/10.1145/3653070)
*来源：作者跟踪: Rui Zhu, Song Gao, Gengchen Mai, Yingjie Hu*

**一句话**：一篇GeoAI领域基础模型的机会与挑战愿景论文，通过七个地理空间任务评测现有大模型并讨论多模态GeoAI基础模型的构建难题。

痛点在于GeoAI领域尚无专门的基础模型，而通用大模型在地理空间任务上的适用性不明。作者在空间语义、健康地理、城市地理、遥感等七个任务上零样本/少样本评测现有基础模型，发现纯文本地理任务上LLM可超越全监督专用模型，但涉及多模态的地理任务（POI城市功能分类、街景噪声分类、遥感场景分类）仍不及专用模型。结论指出构建GeoAI基础模型的核心挑战在于多模态地理数据的对齐与领域知识注入。

> 🔗 **与课题**：与M2路线（Qwen3.5-9B-Base领域继续预训练DAPT+指令SFT）的动机与可行性论证直接相关：论文验证了LLM在文本型地理任务（如地名识别、位置描述理解）上的零样本/少样本优势，可作为GeoAI领域继续预训练的实证支撑与任务选择参考；其七任务评测设计对课题的'GIS评测基准'构建与L3规划层评测有借鉴价值；同时其指出的多模态地理任务短板提示了纯文本GIS工作流自动构建的边界。与M1的IR/KG约束解码、QGIS landing无直接方法关联，主要提供GeoAI基础模型背景与可对比的领域任务清单。

### ⭐⭐⭐ RAG vs Fine-tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture
**6/10** · Angels de Luis Balaguer、Vinamra Benara、Renato L. F. Cunha、Roberto de Moura Estevão Filho、Todd Hendry、Daniel M. Holstein · arXiv (Cornell University) · 2024-01-16 · [原文](https://doi.org/10.48550/arxiv.2401.08406)
*来源：领域×任务*

**一句话**：该论文构建了从PDF抽取到问答生成、微调与GPT-4评估的完整流水线，在农业数据集上系统对比了RAG与微调（含二者叠加）的效果与权衡。

痛点：开发者把专有/领域数据注入LLM时，RAG与微调各自的优劣缺乏系统认识，且评测方法不统一。方法：提出多阶段流水线（PDF信息抽取→自动问答生成→微调→GPT-4打分）与分阶段度量指标，在Llama2-13B、GPT-3.5、GPT-4上做农业（位置相关建议）案例研究。结果：微调带来>6个百分点的准确率提升，RAG再叠加5个百分点，二者互补；并验证了数据生成流水线对地域性知识的捕获能力。

> 🔗 **与课题**：与M2/M3路线的方法论强相关：其"领域数据自动生成指令/QA→微调"流水线可直接借鉴为M2的领域指令SFT与DAPT数据构造方案，其RAG+微调叠加结论可作为M2/M3对比实验与baseline设计依据；其分阶段指标+GPT-4评测思路可用于我的评测层（尤其L3规划与landing的可比评估）。但论文不涉及QGIS/算子链、中间表示、约束解码或工作流生成，与M1架构、KG约束、landing无直接联系；农业+位置相关问答仅弱关联地理领域。

## 📎 5-5 分：备查（26 篇）

### ⭐⭐ LMM Modality Transfer: A Pre-requisite for Autonomous GIS Agents
**5/10** · Ivan Majic、Zexian Huang、Franziska Hübl、Krzysztof Janowicz、Meilin Shi、Mina Karimi · arXiv · 2026-08-07 · [原文](https://arxiv.org/abs/2608.06948v1)
*来源：强命中*

**一句话**：论文提出一个"模态迁移"任务——让一个多模态大模型用文字描述彩色方块网格图像，再由另一个模型实例据文字描述重建原图，以此量化LMM在图像与文本模态间传递空间信息的能力。

痛点在于：现有空间能力研究多局限于纯文本输入输出，而人类做GIS工作流时文本与视觉模态是互补混用的，因此真正的自动化GIS分析管线需要模型能在两种模态间无缝切换。方法上作者设计了一个可量化的模态迁移任务（图像→文本描述→重建图像），并从空间信息理论视角分析LMM的模态对齐能力。结果显示当前先进LMM（如OpenAI系列）在模态迁移上仍表现不佳，说明鲁棒的地理空间理解需要严格的多模态对齐。

> 🔗 **与课题**：与课题在"GIS agent/自动化GIS工作流"这一大方向上相关，也呼应landing层对模型输出可靠性的要求；但它针对的是多模态（图像-文本）对齐瓶颈，不涉及L3操作原语IR、NL2QGIS算子链构建、KG约束解码、DAPT/SFT/QLoRA等具体模块，可作为"多模态GIS agent能力上限"的动机性引用或未来扩展方向，而非可直接对比的基线。

### ⭐⭐ GEEToker for IJGIS
**5/10** · Shuyang Hou · Figshare · 2026-07-01 · [原文](https://doi.org/10.6084/m9.figshare.30408022.v1)
*来源：作者跟踪: 侯舒扬 Hou Shuyang*

**一句话**：该文档是GEEToker项目教程，展示了基于29万条GEE代码样本、经AST解析与中间结构归一化后训练GEE领域专用分词器的完整流程。

痛点：通用分词器（RoBERTa/T5/BERT）对GEE领域代码的切分不理想，缺乏领域词表。方法：从源码去注释→AST解析剪枝→中间结构表示与代码再生→候选核心token抽取与频次过滤→在核心token上训练领域分词器。结果：构建了可复用的GEE代码语料与领域分词器（含100条样例演示，原始数据5.39GB/AST文件245GB）。

> 🔗 **与课题**：与课题的'GEE自动化'与L3中间表示思路相关：其AST→归一化代码→核心token的流水线可作为M2领域继续预训练(DAPT)前的领域分词器与语料构建参考；其中间结构表示与'操作原语IR'思想同源，可作为数据侧基线/预处理模块。但不涉及NL2Code、工作流构建、KG约束解码或评测。

### ⭐⭐ Plan2Map: A Multimodal Benchmark for Document-Grounded Geospatial Boundary Reconstruction from Planning Records
**5/10** · Fabian Degen、Oishi Deb、Jindong Gu、Junchi Yu、Samuele Marro、Philip Torr · arXiv · 2026-06-01 · [原文](https://arxiv.org/abs/2606.02747v1)
*来源：领域×任务*

**一句话**：提出 Plan2Map——一个 208 例的多模态基准，用于从英国规划文档重建地理边界的任务，并给出文档驱动、地理工具在环的 GeoPlanAgent 系统。

痛点：规划记录中的空间约束只能从通知文本、附表、地图图版与标注中间接推断，缺乏机器可读边界，直接让 VLM 输出 GeoJSON 不可靠。方法：作者构建 208 例多模态基准 Plan2Map（参考 GeoJSON 隐藏评测），并提出 GeoPlanAgent，将任务分解为证据抽取、定位、地图配准、边界分割、投影与验证等阶段，地理工具在环调用。结果：GeoPlanAgent 达到 0.736 平均 IoU、0.904 中位 IoU，67.8% 预测 IoU≥0.8，显著优于直接 VLM-to-GeoJSON 基线；诊断显示剩余误差集中在定位与地图配准，监督式边界分割显著提升像素级掩码质量。

> 🔗 **与课题**：主要与评测/agent 编排模块相关：其'工具在环 + 任务分解为可验证阶段'的系统形态，可作为我 M1/M2/M3 路线在 L3→QGIS landing 阶段（多步算子链执行与验证校验）的参考范式；其基准构建思路（输入文档→隐藏参考产物→IoU 等任务级指标）可借鉴到我第三层'最终工作流人工可用率'之外的过程指标设计与评测集构建。差异：它不做自然语言到处理工作流的自动构建，也不涉及算子链顺序、IR、KG 约束解码或 DPO 后训练，故仅可作为 GIS agent + 评测基准的弱相关参考基线。

### ⭐⭐ ecological-agent-skills
**5/10** · Francisco Diego Barros Barata · Zenodo (CERN European Organization for Nuclear Research) · 2026-04-04 · [原文](https://doi.org/10.5281/zenodo.19422444)
*来源：领域×任务*

**一句话**：发布了一个面向定量生态工作流的模块化 AI agent 技能库，包含 17 个技能、14 个工作流和 66 个脚本，支持 Claude Code、Copilot、Cursor 等 agent 框架。

痛点在于生态与地理处理工作流复杂、碎片化且难以复用；作者构建了一个模块化技能库，覆盖数据摄取、地理处理、物种分布建模、占用分析和生态影响评估等任务；成果是 17 技能/14 工作流/66 脚本，提升了 AI agent 在生态工作流中的自动化与可复现报告能力。

> 🔗 **与课题**：与课题中的 GIS agent/copilot、工具调用、workflow 自动构建和 geoprocessing landing 相关，可作为生态地理处理领域的技能/脚本数据资源和 agent 工具调用参考；但不涉及 NL2Code、L3 中间表示、KG 约束解码、QGIS 算子链规划或评测基准，因此不直接支撑 M1/M2/M3 或 KG 约束。

### ⭐⭐ A review of large language models in geomatics: integrating multimodal data, addressing challenges, and exploring synergies
**5/10** · Horia Ameen、Mario Soilán · Spatial Information Research · 2026-02-21 · [原文](https://doi.org/10.1007/s41324-026-00670-3)
*来源：领域×任务*

**一句话**：一篇综述，系统梳理了大语言模型与视觉语言模型在地理信息学（地理空间数据分析与管理、环境与城市规划、遥感）中的应用、多模态数据融合与自主GIS智能体进展及局限。

痛点：卫星影像、LiDAR、众包与传感器等多源地理空间数据快速增长，传统地理信息学方法难以完成集成、解译与自动化。方法：综述性研究，围绕地理空间数据分析与管理、环境与城市规划、遥感三大领域综合已有LLM/VLM应用，并重点评述领域专用copilot、智能体、多模态融合与自主GIS系统，同时批判性讨论算力开销、领域适配与伦理问题。结果：给出当前应用的结构化全景与新兴研究方向，指出语言驱动模型可增强地理信息学方法并重塑空间信息科学的创新与决策。

> 🔗 **与课题**：与课题的GIS agent/copilot、NL2Code、工作流自动构建方向高度同域，可作为M2/M3综述性的相关工作与引用背景，帮助定位'自主GIS/地理空间copilot'的研究现状；但不涉及具体IR设计、约束解码、KG增强、QLoRA微调或可复现评测基准，不能作为方法或对比基线。

### ⭐⭐ The KnowWhereGraph : A Large‐Scale Geo‐Knowledge Graph for Interdisciplinary Knowledge Discovery and Geo‐Enrichment
**5/10** · Rui Zhu、Cogan Shimizu、Shirly Stephen、Colby K. Fisher、Thomas Thelen、Kitty Currier · Transactions in GIS · 2026-02-01 · [原文](https://doi.org/10.1111/tgis.70184)
*来源：作者跟踪: Krzysztof Janowicz(碎片), Wenwen Li, Gengchen Mai*

**一句话**：构建了大规模跨领域地理知识图谱KnowWhereGraph及其配套工具链，用于地理数据集成、丰富与跨学科知识发现。

痛点：现有地理门户数据以孤岛形式堆叠、连接稀疏，难以有效整合复用。方法：以知识图谱为底座，构建预集成、符合FAIR原则、AI-ready的跨域地理数据仓库，强调空间、地点、时间在桥接数据孤岛中的作用，并提供访问与丰富工具。结果：通过多个用例展示该地理知识图谱及其工具如何帮助决策者发现隐藏在异构数据中的洞见。

> 🔗 **与课题**：与KG约束/RAG模块相关：该地理知识图谱提供了地理本体、空间/地点/时间语义schema与跨域实体关系，可作为M1知识图谱约束解码中的类型/关系先验来源，或作为检索增强生成(RAG)的外部地理知识库，也可为landing阶段提供权威地理数据源与I/O类型定义。但其本身不涉及自然语言任务解析、工作流构建或算子链生成，无法作为M1/M2/M3的对比基线。

### ⭐⭐ GLoRA: a novel parameter-efficient fine-tuning framework for GIS large language models
**5/10** · Yifan Zhang、Jingxuan Li、Wenbo Zhang、Zhiyun Wang、Ziyi Zeng、Wei Luo · International Journal of Geographical Information Systems · 2025-12-03 · [原文](https://doi.org/10.1080/13658816.2025.2591830)
*来源：强命中*

**一句话**：提出 GLoRA——一种面向 GIS 大模型的 GIS 知识感知 LoRA 参数分配方案，按层重要性自适应分配可训练参数。

痛点：LoRA 等主流 PEFT 方法对所有层均匀分配参数，忽视了 LLM 各层对 GIS 知识对齐程度不同（部分层已适配良好、部分层仍需大幅调整），可能破坏已适配层或限制待适配层的表达能力。方法：GLoRA 先以数据依赖方式评估各层对给定 GIS 任务的重要性，再动态调整 LoRA 模块规模，把更多参数分给更重要的层。结果：在三个 GIS 相关任务上，在参数量预算相当的情况下优于近期基线。

> 🔗 **与课题**：属于 GIS 领域 LLM 的参数高效微调方法，可对应 M3 路线（官方后训练模型的任务级 QLoRA 微调基线）以及 M2 的领域 SFT 阶段：GLoRA 相比统一秩 QLoRA 的自适应秩/层重要性分配，可作为微调策略的改进项或对比基线；但其研究目标是 GIS 知识对齐与下游 GIS 任务，而非 NL→地理处理工作流生成，也不涉及 L3 中间表示、KG 约束解码、landing 与工作流可用率评测。

### ⭐⭐ MobilityGPT: Enhanced Human Mobility Modeling With a GPT Model
**5/10** · Ammar Haydari、Dongjie Chen、Zhengfeng Lai、Michael Zhang、Chen‐Nee Chuah · IEEE Transactions on Intelligent Transportation Systems · 2025-11-12 · [原文](https://doi.org/10.1109/tits.2025.3626357)
*来源：领域×任务*

**一句话**：提出 MobilityGPT，用 GPT 自回归生成人类移动轨迹，并通过重力采样、路网连通性矩阵约束训练与 RLTF 偏好微调提升地理语义真实性。

痛点：生成式轨迹模型难以保证位置序列语义合理并符合真实地理约束（如路网连通性）。方法：把移动建模重构为自回归生成任务，用基于重力的采样训练序列相似性，用道路连通性矩阵在训练中约束生成，并构建偏好数据集通过轨迹反馈强化学习（RLTF）微调以缩短与真实轨迹的出行距离。结果：在真实数据集上，OD 相似度、行程长度、出行半径、链路等指标优于 SOTA。

> 🔗 **与课题**：该文的'路网连通性矩阵约束生成'与我的 M1 路线中知识图谱约束解码（转移合法性矩阵、I/O 类型约束）在思想与实现层面高度同构，可直接借鉴其如何把结构约束注入生成过程；其'偏好数据集 + 轨迹反馈强化学习微调'与 M2 路线的过程监督/偏好后训练（DPO 类）思路一致，可作为领域偏好数据构造与奖励设计的参考；此外它属于地理空间序列生成而非代码/工作流生成，故与 NL2GIS 工作流构建、L3 原语 IR、landing 与评测基准仅有间接迁移价值，可作为'约束生成+偏好后训练'方向的可对比旁证基线。

### ⭐⭐ Automating Geospatial Vision Tasks with a Large Language Model Agent
**5/10** · Yuxing Chen、Weijie Wang、Camille Kurtz、Sylvain Lobry · Lecture notes in computer science · 2025-10-03 · [原文](https://doi.org/10.1007/978-3-662-72243-5_13)
*来源：领域×任务*

**一句话**：该论文提出用大语言模型智能体自动完成地理空间视觉任务（遥感影像分析类任务）的流程编排与执行。

痛点：地理空间视觉任务（如遥感影像分类、目标检测、变化检测）通常需要专家手工选择模型、配置参数并串联处理步骤，门槛高且难以复用。方法：论文将 LLM 作为智能体（agent）来理解任务描述、规划并调用地理空间视觉算子/工具，自动构建处理流程。结果：摘要未给出（来源仅为标题），但从标题可知其完成了地理空间视觉任务的自动化编排尝试。

> 🔗 **与课题**：与课题同为“自然语言任务描述 → 自动构建地理空间处理流程”的 GIS agent 思路，可作为 M3 路线（官方后训练模型做任务级/智能体式适配）与 baseline 的参考；但其聚焦遥感视觉任务而非 QGIS 地理处理算子链，对 L3 平台无关原语 IR、KG 约束解码、landing 与评测模块直接借鉴有限。注：本条目未提供摘要，判断主要依据标题。

### ⭐⭐ Fusing Geoscience Large Language Models and Lightweight RAG for Enhanced Geological Question Answering
**5/10** · Bo Zhou、Ke Li · Geosciences · 2025-10-02 · [原文](https://doi.org/10.3390/geosciences15100382)
*来源：领域×任务*

**一句话**：该文用领域大模型 GeoGPT 自动构建矿产勘查知识图谱，并结合轻量级 LightRAG 双层次检索搭建地质问答系统。

痛点：通用 LLM 难以理解地质文本的专业词汇与关系语义，导致领域知识图谱构建质量差、问答精度低。方法：以领域模型 GeoGPT 完成本体定义、实体识别与关系抽取来自动建 KG，再用 LightRAG 的双层检索与增量更新机制驱动地质问答。结果：实体抽取平均 F1 达 0.835（较通用大模型提升 17%–25%），地质问答在地球化学与遥感地质领域相对 DeepSeek-V3、Qwen2.5-72B 胜率分别高出 8–29% 与 53–78%。

> 🔗 **与课题**：与 M2 领域继续预训练路线相关（GeoGPT 属地理领域适配的领域 LLM，可参考其 DAPT/领域数据构建与评测方式）；其“LLM 自动构建领域 KG + RAG 检索增强”范式可为 M1 的知识图谱约束解码/外部知识注入提供思路与可借鉴流程；地质问答胜率评测方法可作 geoscience 领域评测基准与人工/模型对比评估的参考。但不涉及 GIS 算子工作流自动构建、NL2Code、IR 中间表示或 QGIS landing。

### ⭐⭐ A Spatio-Temporal Evolutionary Embedding Approach for Geographic Knowledge Graph Question Answering
**5/10** · Chunju Zhang、Chaoqun Chu、Kang Zhou、Shu Wang、Yunqiang Zhu、Jianwei Huang · ISPRS International Journal of Geo-Information · 2025-07-28 · [原文](https://doi.org/10.3390/ijgi14080295)
*来源：领域×任务*

**一句话**：提出 ST-EKA 时空演化知识嵌入方法，通过类型感知编码、时空衰减与注意力上下文聚合提升 GeoKG 表示学习和地理知识图谱问答性能。

现有知识图谱嵌入多关注结构模式，忽略地理实体在时间和空间上的动态演化，限制下游推理与问答。ST-EKA 融合关系类型一致编码、时间点/区间统一编码、多尺度空间编码和注意力时空加权，在 GDELT、ICEWS、HAD 上提升表示学习与问答指标。结果表明其在链式查询和复杂时空推理上更优。

> 🔗 **与课题**：与 KG 约束/知识图谱增强生成相关：其地理知识图谱嵌入和时空推理可作为 QGIS 工作流中地理实体/关系语义表示与知识约束解码的知识源或推理基线；但它不涉及 NL2Code、工作流自动构建、IR 设计、QGIS landing、DPO 或工具调用，因此与 M1/M2/M3 主线为弱相关。

### ⭐⭐ MapBot: A Multi-Modal Agent for Geospatial Analysis
**5/10** · Martin Weiss、Nasim Rahaman、Chris Pal · 预印本 · 2025-05-28 · [原文](https://doi.org/10.65109/hfzd6332)
*来源：领域×任务*

**一句话**：MapBot 是一个多模态地理空间分析智能体，用 LLM 在 REPL 循环中编排 Segment Anything、DinoV2 等视觉模型并生成执行 Python 代码，支持用户通过对话和点选交互完成影像标注与查询。

痛点：地理空间分析门槛高，非专家难以对遥感影像做标注、查询与分析。方法：将前沿 CV 模型与 LLM 结合，LLM 在 Read-Eval-Print Loop 中生成并执行 Python 代码，编排 Segment Anything、DinoV2 等工具，并通过 Web 界面呈现结果，支持自然语言 + 点选的多模态交互。结果：实现了对话式、可交互的地理空间数据处理系统，降低非专家的使用门槛。

> 🔗 **与课题**：属于 GIS agent/copilot 与 geospatial code generation 方向，可作为 M1/M2 之外'LLM Agent + 工具编排 + 代码生成执行'的对比基线或相关工作参考；其 REPL 式代码生成—执行闭环与我的 L3→QGIS landing、工具调用环节思路相近，但未涉及操作原语中间表示、知识图谱约束解码、工作流顺序构建与专门评测基准，因此相关性中等。

### ⭐⭐ Beyond words: evaluating large language models in transportation planning
**5/10** · Shaowei Ying、Zhenlong Li、M. Yu · Geo-spatial Information Science · 2025-04-30 · [原文](https://doi.org/10.1080/10095020.2025.2493073)
*来源：作者跟踪: Zhenlong Li*

**一句话**：该研究用三层评估框架（地理空间技能、交通领域知识、真实拥堵收费决策）测试 GPT-4 与 Phi-3-mini 在交通规划决策中的知识、推理与工作流设计与执行能力。

痛点在于 LLM 能否胜任城市交通规划这类需要领域知识加空间分析工作流的决策任务尚无系统评估。作者提出 H1（通用 LLM 具备基础交通知识与工作流设计执行能力）与 H2（大参数与微调模型优于小模型）两条假设，用地理空间技能、MATSim 等交通领域理解、真实拥堵收费问题解决三个层级评测 GPT-4 与 Phi-3-mini。结果显示 LLM 具备基线地理空间与交通推理能力但随任务复杂度波动，GPT-4 在 GIS 任务 86%、MATSim 理解 81%、决策支持 91%，Phi-3-mini 仅 43–72%，支持大模型作为规划分析 copilot 的潜力。

> 🔗 **与课题**：与课题的评测模块（三层评估中的 L3 规划与 landing 可用率）和方法论最相关：其"三层评估框架"可作为我 L3/L3→QGIS/人工可用率评估设计的对照参考；其"大模型 vs 小模型/微调模型"结论可支持我 M2（领域继续预训练+SFT）与 M3（QLoRA 微调基线）的合理性论证，并作为任务级 LLM 评测的可对比基线（baseline）；但它不涉及 QGIS 工作流自动构建、IR、KG 约束解码或工具调用落地，因此对 M1 架构与 KG 约束几乎无直接贡献。

### ⭐⭐ Evaluating and enhancing spatial cognition abilities of large language models
**5/10** · Anran Yang、Cheng Fu、Qingren Jia、Weihua Dong、Mengyu Ma、Hao Chen · International Journal of Geographical Information Systems · 2025-04-15 · [原文](https://doi.org/10.1080/13658816.2025.2490701)
*来源：领域×任务*

**一句话**：论文构建了评估大模型空间认知能力的七类基准，并提出 Hybrid Mind 工具增强方法，将 LLM 与确定性 GIS 算法结合以提升空间认知任务表现。

痛点在于现有研究多关注小规模感知，缺乏对 LLM 在 GIScience 场景中空间认知能力的系统评估。方法上提出七类空间认知基准，并设计 Hybrid Mind：用确定性 GIS 算法与 mental map builder 将定性约束转为定量地图，弥补 LLM 合成空间信息时的错误。结果显示 LLM 在路线与 survey knowledge 等任务上表现很差，GPT-4-turbo 正确率不足四分之一，而 Hybrid Mind 显著提升至约 70%。

> 🔗 **与课题**：与课题在“LLM + 确定性 GIS 算法/工具增强”“GIS 任务评测基准设计”“neuro-symbolic 约束求解”上相关，可为 GIS agent/copilot 的工具调用、LLM 与 GIS 算子混合求解、以及你的三层评测提供基准设计思路和可参考的 tool-augmented 对比基线；但不涉及 QGIS 工作流自动构建、L3 中间表示、KG 约束解码、DPO 或 QLoRA 微调。

### ⭐⭐ Evaluating large language models on geospatial tasks: a multiple geospatial task benchmarking study
**5/10** · Liuchang Xu、Shuo Zhao、Qingming Lin、Luyao Chen、Qianqian Luo、Sensen Wu · International Journal of Digital Earth · 2025-04-06 · [原文](https://doi.org/10.1080/17538947.2025.2480268)
*来源：领域×任务*

**一句话**：构建覆盖12类地理空间任务的多任务评测数据集，并系统评测GPT-3.5/GPT-4/GPT-4o/GLM-4/Claude-3等大模型在零样本与提示调优下的表现。

痛点：大语言模型在地理空间任务上的能力尚未被充分评估。方法：提出包含空间理解、路径规划等12类任务、答案经校验的多任务空间评测数据集，采用零样本测试与基于难度的提示调优两阶段评估多个主流模型。结果：gpt-4o零样本总体准确率最高(71.3%)，moonshot-v1-8k在地名识别上更优，且CoT提示把gpt-4o路径规划准确率从12.4%提升至87.5%，说明提示策略影响显著。

> 🔗 **与课题**：与课题的评估层相关：可作为地理空间LLM能力评测基准与GPT/GLM/Claude等通用模型基线，用于横向对比M2(DAPT+SFT)、M3(QLoRA微调)模型的地理任务能力；但该基准为问答式空间理解与路径规划，不涉及地理处理工作流自动构建、L3 IR规划、KG约束解码或QGIS landing，故与核心工作流构建方法无直接联系。

### ⭐⭐ GeoRAG: A Question-Answering Approach from a Geographical Perspective
**5/10** · Jian Wang、Zhuo Zhao、Zeng Jie Wang、Bo Da Cheng、Lei Nie、Wen Luo · arXiv · 2025-04-02 · [原文](https://arxiv.org/abs/2504.01458v2)
*来源：强命中*

**一句话**：构建了面向地理问答的 GeoRAG 框架，用结构化地理知识库 + BERT 查询分类 + 检索评估器 + 提示模板来增强地理知识检索与问答。

痛点：传统地理问答系统理解能力弱、检索精度低、交互性差，难以处理复杂地理查询。方法：从 3267 篇语料出发，用多智能体将地理知识按语义理解、空间位置、几何形态、属性特征、要素关系、演化过程、作用机制七个维度结构化，构建 145234 条知识条目与 875432 条多维 QA 对；再用 BERT-Base-Chinese 多标签分类器判定查询维度，配合检索相关性评估器与 GeoPrompt 模板做 RAG 增强。结果：提升了地理领域知识检索精度与响应质量。

> 🔗 **与课题**：与 KG 约束/KG 增强生成、RAG 模块相关：其「地理七维知识分类体系 + 结构化地理知识库」可作为我知识图谱约束解码中地理概念层级与类型约束的来源；BERT 多标签查询分类器与检索评估器可作为我 M1 中「文本编码 + 输入需求解析」以及 RAG 检索质量过滤的参考组件；其多维 QA 对构造流程（多智能体标注）对我 M2 领域指令 SFT 数据构造与 LLM 合成数据管线有直接借鉴价值。但该文只做地理问答，不涉及工作流/算子链生成、IR、受限解码或 QGIS landing，无法作为工作流生成的可比基线。

### ⭐⭐ Intelligent determination of proper spatial extents for input data during geographical model workflow building
**5/10** · Z. T. Chen、Cheng‐Zhi Qin、Liang‐Jun Zhu、Chenglong Wu、Yingchao Ren、A‐Xing Zhu · Environmental Modelling & Software · 2025-02-11 · [原文](https://doi.org/10.1016/j.envsoft.2025.106369)
*来源：领域×任务*

**一句话**：该论文研究在地理模型工作流构建过程中智能地为输入数据确定合适的空间范围（extent）。

痛点在于地理建模工作流搭建时，输入数据的空间范围往往依赖人工经验判断，选错范围会导致计算浪费或结果不可用。作者提出一种智能化的空间范围确定方法，服务于地理模型工作流的自动/半自动构建流程。论文发表在 Environmental Modelling & Software，属于地理建模工作流自动化方向的期刊工作（因未提供摘要，具体方法细节未知）。

> 🔗 **与课题**：与课题中 L3→QGIS landing 环节相关：工作流从操作原语落地到具体 QGIS 算子链时，需要为每个算子确定输入数据的空间范围/数据对象，这正是 I/O 约束与数据准备的一部分，可作为 landing 阶段输入数据自动配置模块的参考或对比工作；但不涉及 NL2Code、约束解码或 KG 增强生成等核心方法模块。

### ⭐⭐ HGeoKG: A Hierarchical Geographic Knowledge Graph for Geographic Knowledge Reasoning
**5/10** · T. Li、Renyao Chen、Yilin Duan、Hong Yao、Shengwen Li、Xinchuan Li · ISPRS International Journal of Geo-Information · 2025-01-03 · [原文](https://doi.org/10.3390/ijgi14010018)
*来源：强命中*

**一句话**：该论文构建了分层地理知识图谱 HGeoKG 并发布 67 万级数据集 HGeoKG-MHT-670K，用于地理知识推理评测。

现有地理知识图谱缺乏层次化建模、实体类型/属性/空间关系覆盖不足，难以支撑语义互操作与表示。作者提出分层 GeoKG 建模框架（层次结构+属性+空间关系），据此构建 HGeoKG-MHT-670K 数据集，并发现其呈明显区域异质性与长尾分布。在推理实验中多数 KGE 模型表现不佳，说明需针对空间异质性与长尾实体改进嵌入，同时该数据集可作为地理知识推理基准。

> 🔗 **与课题**：与 M1 路线的知识图谱约束解码直接相关：其分层地理实体/属性/空间关系建模思路可借鉴用于构建面向 QGIS 操作原语与地理概念的知识图谱，为转移合法性矩阵与 I/O 类型约束提供地理语义侧支撑；HGeoKG-MHT-670K 可作为地理领域知识注入/评测的数据资源，也提示长尾与区域异质性问题在 KG 约束解码与领域预训练(M2)中需处理。但该文不涉及工作流生成、NL2Code 或 GIS 算子落地，不能作为 landing/端到端工作流基线。

### ⭐⭐ MME: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models
**5/10** · Chaoyou Fu、Peixian Chen、Yunhang Shen、Yulei Qin、Mengdan Zhang、Lin Xu · 预印本 · 2025-01-01 · [原文](https://doi.org/10.52202/085713-4899)
*来源：强命中*

**一句话**：论文评测了 GPT-3.5/4、LLaMA2.0、Falcon40B 四款 LLM 在空间计算、地理概念问答与地理代码生成任务上的能力差异。

痛点在于尚不清楚 LLM 能正确回答哪些空间问题、能否进行空间推理，以及不同模型间的能力差异。作者设计了一套可扩展的评测方法，让四个 LLM 回答从基础空间计算到高级地理概念的问题，并考察其代码生成与文字解释能力。结果显示模型在基础问题上表现较好，而面对高级空间概念时结果参差不齐，为后续测试与微调策略提供了参考。

> 🔗 **与课题**：与课题的 evAl 层最相关：其对 LLM 地理问答/地理代码生成的评测设计与‘不同模型能力差异’分析，可为我的 L3 规划与 landing 评测指标设计提供参考，并提供 GPT/LLaMA/Falcon 等可作为 M3 类基线模型的横向对比数据；但未涉及工作流自动构建、IR、KG 约束解码或微调方法。

### ⭐⭐ Answering Complex Geographic Questions by Adaptive Reasoning with Visual Context and External Commonsense Knowledge
**5/10** · Fan Li、Jianxing Yu、Jielong Tang、Wenqing Chen、Hanjiang Lai、Yanghui Rao · 预印本 · 2025-01-01 · [原文](https://doi.org/10.18653/v1/2025.acl-long.1239)
*来源：强命中*

**一句话**：该论文提出一种自适应推理框架，融合视觉上下文与外部常识知识来回答复杂地理问题。

痛点：复杂地理问答需要多跳推理，且依赖图外常识与视觉线索，纯文本模型难以胜任。方法：作者设计自适应推理机制，动态决定何时引入视觉上下文与外部常识知识（可能以知识库/图谱形式）进行多步推理。结果：在 ACL 2025 发表，在地理问答任务上验证了该框架的有效性（摘要未给出具体指标）。

> 🔗 **与课题**：属于地理问答/地理知识增强推理方向，与课题的相关性主要在 KG 约束解码与评测层面：其“外部常识知识 + 自适应多步推理”可类比课题中知识图谱增强生成与转移合法性约束的思路，其地理问答数据集/评测协议可作为领域理解能力与推理链正确性的参考基准；但与 QGIS 工作流构建、L3 中间表示、NL2Code 算子链生成无直接关系。

### ⭐⭐ Generating a Question Answering Dataset About Geographic Changes in a Knowledge Graph
**5/10** · Michail Mitsios、Dharmen Punjani、Sara Abdollahi、Simon Gottschalk、Eleni Tsalapati、Elena Demidova · Lecture notes in computer science · 2024-11-20 · [原文](https://doi.org/10.1007/978-3-031-77792-9_28)
*来源：领域×任务*

**一句话**：该论文构建了一个面向知识图谱中地理变化信息的问答数据集。

论文关注地理变化信息在知识图谱中难以直接问答的问题，提出生成相关问答数据集的方法。其核心围绕知识图谱与地理问答数据构建，可能支持地理变化查询与评测。由于摘要缺失，具体方法与结果无法确认，但从标题看属于地理知识图谱与问答数据集工作。

> 🔗 **与课题**：与课题在地理知识图谱、地理问答评测数据构建相关，可为KG约束、评测数据构造提供参考；但不涉及NL2Code、QGIS工作流自动生成或GIS agent/copilot。相关模块：KG、data、eval。

### ⭐⭐ The question answering system GeoQA2 and a new benchmark for its evaluation
**5/10** · Sergios-Anestis Kefalidis、Dharmen Punjani、Eleni Tsalapati、Konstantinos Plas、Maria-Aggeliki Pollali、Pierre Maret · International Journal of Applied Earth Observation and Geoinformation · 2024-10-16 · [原文](https://doi.org/10.1016/j.jag.2024.104203)
*来源：领域×任务*

**一句话**：提出了地理问答引擎GeoQA2和包含1089个自然语言问题及其SPARQL/GeoSPARQL查询和答案的数据集GeoQuestions1089，并进行了对比评估。

痛点：地理问答系统缺乏统一评测基准，现有系统性能不足。方法：构建GeoQA2引擎在YAGO2和YAGO2geo知识图谱上回答地理空间问题，并发布GeoQuestions1089数据集，包含自然语言问题、对应SPARQL/GeoSPARQL查询及答案。结果：GeoQA2优于Hamzei et al. 2022的系统，但两者均有较大提升空间。

> 🔗 **与课题**：与课题中KG约束解码和地理知识图谱增强生成相关；GeoQuestions1089可作为NL→GeoSPARQL语义解析的评测数据集，用于评估L3规划或M1/M2模型在KG查询生成任务上的表现；可作为KG-based QA的对比基线。

### ⭐⭐ ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery
**5/10** · Ziru Chen、Shijie Chen、Yuting Ning、Qianheng Zhang、Boshi Wang、Botao Yu · arXiv (Cornell University) · 2024-10-07 · [原文](https://doi.org/10.48550/arxiv.2410.05080)
*来源：作者跟踪: Song Gao*

**一句话**：构建了 ScienceAgentBench 基准，从 44 篇同行评审论文中抽取 102 个数据驱动科学发现任务，统一为自包含 Python 程序，并系统评测五种 LLM 在三种 agent 框架下的表现。

痛点：LLM agent 宣称能端到端自动化科学发现，但缺乏严格、可验证的任务级评测。方法：从四个学科的 44 篇论文中提取 102 个任务，经九位领域专家多轮人工校验，统一输出为独立 Python 程序，并设计执行结果、程序质量与成本等多维指标，同时提出两种缓解数据污染的策略；在 direct prompting、OpenHands CodeAct、self-debug 三种框架下评测五个开源/闭源 LLM。结果：每题三次尝试下最佳 agent 仅独立解决 32.4% 任务，专家提供知识后也仅 34.3%，说明任务级自动化仍远未成熟。

> 🔗 **与课题**：与课题的 eval 模块直接相关：其“任务级、执行结果导向、多次尝试+成本”的评测设计与我的三层评估（L3 规划 / landing / 人工可用率）思路可类比，可借鉴其任务抽取、专家校验与污染控制流程来设计 QGIS 工作流评测基准；self-debug 框架对应我的分级回退修复机制，可作为对照基线；且其结论（agent 独立完成率低、需外部知识）可支撑我引入 KG 约束解码与领域知识的动机。但与 GIS/地理处理、IR 中间表示、QGIS landing 无直接关系。

### ⭐⭐ GEUKE : A geographic entities uniformly explicit knowledge embedding model
**5/10** · Yongquan Yang、Dehui Kong、Min Cao、Min Chen · Transactions in GIS · 2024-05-28 · [原文](https://doi.org/10.1111/tgis.13191)
*来源：领域×任务*

**一句话**：提出 GEUKE 地理实体统一显式知识嵌入模型，用基于 SubGNN 的空间特征编码器把点/线/面实体的空间嵌入与结构嵌入统一到同一向量空间。

痛点：地理知识图谱中知识嵌入需兼顾点、线、面多类型实体的空间特征表达，已有 TransE 系方法难以统一编码并保留位置、邻域与结构属性。方法：将点线面地理实体表示为子图，用 SubGNN 统一空间特征编码器生成空间嵌入，并改造 TransE 的能量函数，将空间特征嵌入与结构嵌入联合训练到统一向量空间。结果：在链接预测与三元组分类任务上优于 TransE、TransH、TransD、TransE-GDR，且能保持三类实体的固有空间特征与相互关系。

> 🔗 **与课题**：与 KG 约束/知识图谱增强模块相关：可为我的知识图谱约束解码提供地理实体（点/线/面）及其关系的向量化表示与合法性推理基础，用于转移合法性矩阵或 I/O 类型约束的知识来源；但不涉及工作流构建、NL2Code、IR 或 QGIS/GEE 算子链，与 M1/M2/M3 三条模型路线无直接可比性。

### ⭐⭐ Is ChatGPT a Good Geospatial Data Analyst? Exploring the Integration of Natural Language into Structured Query Language within a Spatial Database
**5/10** · Yongyao Jiang、Chaowei Yang · ISPRS International Journal of Geo-Information · 2024-01-10 · [原文](https://doi.org/10.3390/ijgi13010026)
*来源：领域×任务*

**一句话**：提出并验证了一个用 LLM 将自然语言问题转为空间数据库 SQL 查询、再把结果解析回自然语言的框架，在真实数据上测试了空间连接等查询。

痛点：传统上与地理空间数据交互依赖 ArcGIS、Python 等专业工具与语言，门槛高，缺乏自然语言接口。方法：作者设计四步框架——训练 LLM 理解数据集、依据自然语言问题生成地理空间 SQL、发送给后端空间数据库、再把数据库响应解析回人类语言，并以真实数据做案例研究。结果：LLM 在包括空间连接的大多数查询上能较准确生成 SQL，但仍有改进空间；作者认为该框架可作为自动化地理空间分析的通用代理。

> 🔗 **与课题**：与课题的 NL2Code / GIS copilot 方向及'landing'环节相关：它给出自然语言→领域代码（此处为空间 SQL 而非 QGIS 处理算子链）的映射与执行-回译闭环，可作为 L3 规划落地到具体地理计算后端时的对比基线；其'先让模型理解数据集模式再生成代码'的思路可借鉴到我的 I/O 类型约束与 QGIS 算子参数化中。但该工作只做单条 SQL 生成、无算子链/工作流顺序、无知识图谱或约束解码、无过程监督与工作流可用率评测，与 M1 的 IR 解码、KG 合法性约束及三层评测体系关联较弱。

### ⭐⭐ Interactive technology for the generation of spatial data processing workflows
**5/10** · R.V. Brezhnev、Yu.A. Maglinets、N.S. Khorosheva、К.В. Раевич · Sovremennye problemy distantsionnogo zondirovaniya Zemli iz kosmosa · 2024-01-01 · [原文](https://doi.org/10.21046/2070-7401-2024-21-2-89-100)
*来源：领域×任务*

**一句话**：提出一种交互式技术，辅助用户生成空间数据处理工作流（俄文期刊论文，摘要截断）。

痛点：空间数据（遥感/GIS）处理流程构建复杂，非专家难以自行组装正确的处理链。方法：作者提出交互式技术，通过人机交互引导用户逐步形成空间数据处理工作流（workflow），强调流程生成的可用性与可操作性。结果：摘要信息不完整，未能获取具体实验与定量结果，但从题名与来源看属于遥感/GIS 工作流构建工具的工程性研究。

> 🔗 **与课题**：与课题中「自然语言任务描述→自动构建 QGIS 地理处理工作流」的目标场景直接相关，可作为 GIS 工作流自动/半自动构建的相关工作与可对比基线（交互式 vs. 端到端自动生成）；但其为交互式（human-in-the-loop）路线，不涉及 LLM/NL2Code、IR 中间表示、KG 约束解码或 DPO 后训练，因此主要关联 landing 与评测层的工作流可用性讨论，对 M1/M2/M3 技术路线参考价值有限。
