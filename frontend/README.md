# Travel-Agent 前端工程

基于 AI 的个性化旅行行程规划前端应用。
本前端工程完全由AI实现，开发工具使用Claude Code + Minimax

## 技术栈

| 技术 | 版本 | 用途 |
|-----|------|------|
| Vue | 3.4.x | 前端框架 |
| TypeScript | 5.2.x | 类型安全 |
| Vite | 5.1.x | 构建工具 |
| Ant Design Vue | 4.1.x | UI 组件库 |
| Axios | 1.6.x | HTTP 客户端 |
| Vue Router | 4.3.x | 路由管理 |

## 启动方式

```bash
cd frontend
npm install
npm run dev
```

开发服务器运行在 http://localhost:5173

## 项目结构

```
frontend/
├── index.html              # 入口 HTML
├── package.json            # 项目配置
├── vite.config.ts          # Vite 配置
├── tsconfig.json           # TypeScript 配置
├── env.d.ts                # 类型声明
└── src/
    ├── main.ts             # 应用入口
    ├── App.vue             # 根组件
    ├── style.css           # 全局样式
    ├── api/
    │   └── index.ts        # API 服务封装
    ├── router/
    │   └── index.ts        # 路由配置
    └── components/
        └── TravelForm.vue  # 主表单组件
```

## 开发历程

### 1. 工程初始化

**用户提问**: 使用Vue3、TypeScript、Vite、Ant Design Vue、Axios、Vue Router实现一个前端工程，直接创建在frontend中

**实现内容**:
- 创建 package.json，配置所有依赖
- 创建 Vite + TypeScript 构建配置
- 创建 Vue3 + Vue Router 项目架构
- 实现主表单组件 TravelForm.vue

### 2. 配置文件简化

**用户提问**: 三个tsconfig的作用是什么，有什么区别？可以只保留一个tsconfig

**回答**: 解释了 tsconfig.json（主配置）、tsconfig.node.json（Node环境）、tsconfig.app.json（应用配置）的区别，最终简化为只保留一个 tsconfig.json。

### 3. API 接口调整

**用户提问**: 向后端发送请求的地址是 /api/trip/plan

**修改内容**: 将 API 请求地址从 `/generate-itinerary` 改为 `/trip/plan`。

### 4. 响应格式适配

**用户提问**: 后端返回的响应格式...

**修改内容**:
- 定义完整的 TypeScript 类型接口（TripPlanResponse、DayPlan、Attraction、Meal、Hotel 等）
- 修改 TravelForm.vue 组件以结构化方式展示后端返回数据

### 5. 前后端字段对齐

**用户提问**: 阅读 schemas.py 文件，保持前端请求和响应和后端一致

**修改内容**:
| 后端字段 | 修改前 | 修改后 |
|---------|--------|--------|
| destination | city | city |
| preferences | string | string[] |
| extra_requirements | free_text_input | free_text_input |
| 旅行偏好 | 文本输入 | 多选下拉框 |

## 功能特性

- 目的地城市输入
- 开始/结束日期选择（自动计算旅行天数）
- 旅行天数输入
- 交通方式选择
- 住宿偏好选择
- 旅行偏好多选
- 额外要求文本输入
- AI 行程生成结果展示（结构化显示每日行程、景点、餐饮、住宿、天气、预算等）

## 构建部署

```bash
npm run build
```

构建产物为纯静态文件，可部署到任意静态服务器。

## 代理配置

开发环境通过 Vite 代理将 `/api` 请求转发到后端服务：

```typescript
// vite.config.ts
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:8000',
      changeOrigin: true
    }
  }
}
```
