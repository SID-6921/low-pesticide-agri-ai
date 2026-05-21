from collections import deque

from app.models.schemas import PathPlanRequest


MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def plan_path(req: PathPlanRequest) -> dict:
    blocked = set(req.blocked)
    start = req.start
    goal = req.goal

    q = deque([start])
    visited = {start}
    parent: dict[tuple[int, int], tuple[int, int] | None] = {start: None}

    while q:
        x, y = q.popleft()
        if (x, y) == goal:
            break
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < req.rows and 0 <= ny < req.cols):
                continue
            if (nx, ny) in blocked or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            parent[(nx, ny)] = (x, y)
            q.append((nx, ny))

    if goal not in parent:
        return {"path": [], "distance": None, "status": "unreachable"}

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return {"path": path, "distance": len(path) - 1, "status": "ok"}
