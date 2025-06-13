import Cookies from "js-cookie";

async function updatePost(url, { arg }: { arg: string }) {
    const res = await fetch(url, {
        mode: "cors",
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`
        },
        body: JSON.stringify({post_content: arg})
    })
    return await res.json();
}

export default updatePost;