import os
import pytest

"""
使用方法：

1. 运行当前 E2E 测试：
    cd backend
    RUN_E2E=1 pytest test/test_plan_trip.py::test_plan_trip_end_to_end -s
"""

RUN_E2E = os.getenv("RUN_E2E", "0") == "1"

pytestmark = pytest.mark.skipif(
    not RUN_E2E, reason="Set RUN_E2E=1 to run end-to-end tests"
)

# 定义 TestClient fixture
@pytest.fixture(scope="module")
def client():
    """提供 FastAPI TestClient 实例，供测试函数复用"""
    from fastapi.testclient import TestClient
    from app.api.main import app  # 导入你的 FastAPI app

    with TestClient(app) as c:
        yield c


# 测试函数
def test_plan_trip_end_to_end(client):
    """端到端测试：POST /api/trip/plan"""
    payload = {
        "city": "北京",
        "start_date": "2026-01-20",
        "end_date": "2026-01-23",
        "travel_days": 3,
        "transportation": "公共交通",
        "accommodation": "经济型酒店",
        "preferences": ["历史文化", "美食"],
        "free_text_input": "希望多安排博物馆",
    }

    # 发起 POST 请求
    resp = client.post("/api/trip/plan", json=payload)

    # ✅ 检查 HTTP 状态码
    assert resp.status_code == 200, f"请求失败: {resp.text}"

    # ✅ 解析响应 JSON
    body = resp.json()
    assert body.get("success") is True
    assert body.get("data") is not None
