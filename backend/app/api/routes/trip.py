from fastapi import APIRouter, HTTPException
from ...models.schemas import (
    TripRequest,
    TripPlanResponse,
    ErrorResponse
)
from ...agents.langgraph import agent_plan_trip

router = APIRouter(prefix="/trip", tags=["旅行规划"])

@router.post(
    "/plan",
    response_model=TripPlanResponse,
    summary="生成旅行计划",
    description="根据用户输入的旅行需求,生成详细的旅行计划"
)
async def plan_trip(request: TripRequest):
    """
    生成旅行计划

    Args:
        request: 旅行请求参数

    Returns:
        旅行计划响应
    """
    try:
        print(f"\n{'='*60}")
        print(f"📥 收到旅行规划请求:")
        print(f"   城市: {request.city}")
        print(f"   日期: {request.start_date} - {request.end_date}")
        print(f"   天数: {request.travel_days}")
        print(f"{'='*60}\n")

        # 生成旅行计划
        print("🚀 开始生成旅行计划...")
        trip_plan = await agent_plan_trip(request)

        print("✅ 旅行计划生成成功,准备返回响应\n")

        resp = TripPlanResponse(
            success=True,
            message="旅行计划生成成功",
            data=trip_plan
        )
        try:
            print("🖨️ 返回 TripPlanResponse:")
            print(resp.model_dump_json(ensure_ascii=False, indent=2))
        except Exception:
            print(repr(resp))
        return resp

    except Exception as e:
        print(f"❌ 生成旅行计划失败: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"生成旅行计划失败: {str(e)}"
        )
