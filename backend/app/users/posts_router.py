from fastapi import APIRouter, HTTPException, Depends, status
from app.users.schema import IdUser, CreateUserPost, UpdateUserPost, IdPost
from app.db import posts_sql as db_posts
from app.users import dependencies as dep
from app.config import settings
from app.db import friends_sql as db_friends
import httpx

router = APIRouter()


@router.get("/user/posts")
def get_user_posts(token: str = Depends(dep.get_token)):
    user_id = dep.get_current_user(token)

    try:
        return db_posts.get_user_posts(user_id)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Posts not found"
        )


@router.post("/post/create")
def create_user_post(post: CreateUserPost, token: str = Depends(dep.get_token)):
    user_id = dep.get_current_user(token)

    try:
        db_posts.create_user_post(user_id, post.post_content)
        return {"Post Create:", "ok"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User post can create"
        )


@router.post("/post/create/ws")
def fetch_external_data(user_id: IdUser):
    ws_notification = (f"http://{settings.POST_NOTIFICATION_HOST}:{settings.POST_NOTIFICATION_PORT}"
                        f"/post/feed/posted?user_id={user_id.id}")

    result = [i[1] for i in db_friends.get_user_friends(user_id.id)]

    if result:
        httpx.post(ws_notification, json={"id": user_id.id, "user_friends": result})


@router.post("/post/update")
def update_user_post(update_post: UpdateUserPost, token: str = Depends(dep.get_token)):
    try:
        db_posts.update_user_post(update_post.id, update_post.post_content)
        return {"Post Update:", "ok"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Post can Update"
        )


@router.post("/post/delete")
def delete_user_post(id_post: IdUser, token: str = Depends(dep.get_token)):
    user_id = dep.get_current_user(token)
    try:
        db_posts.delete_user_post(user_id, id_post.id)
        return {"Post Delete:", f"{id_post}"}
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Post not Delete"
        )


@router.get("/post/get")
def get_user_post_by_id(id_post: int):
    try:
        return db_posts.get_user_post_by_id(id_post)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not Found"
        )


@router.get("/post/feed")
def get_post_limit_and_offset(post_limit: int, offset: int, token: str = Depends(dep.get_token)):
    user_id = dep.get_current_user(token)
    try:
        return db_posts.get_post_limit_and_offset(user_id, post_limit, offset)
    except BaseException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Posts not Found"
        )
