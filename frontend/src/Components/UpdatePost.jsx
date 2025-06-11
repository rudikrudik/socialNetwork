import Cookies from "js-cookie";

async function updatePost(url, { arg }: { arg: string }) {
    const res = await fetch(url, {
        mode: "cors",
        method: 'POST',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            Cookies: `user_access_token=${Cookies.get('user_access_token')}`,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({post_content: arg})
    })
    return await res.json();
}

export default updatePost;