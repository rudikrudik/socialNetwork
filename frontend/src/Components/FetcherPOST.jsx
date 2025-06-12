import Cookies from "js-cookie";

const fetcherPost = async (url, body) => {
    const res = await fetch(url, {
        mode: "cors",
        method: 'POST',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`
        },
        body: JSON.stringify(body)
    },);

    return await res.json();
};

export default fetcherPost;