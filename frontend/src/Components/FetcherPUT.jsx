import Cookies from "js-cookie";

const fetcherPUT = async (url) => {
    const res = await fetch(url, {
        mode: "cors",
        method: 'PUT',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`
        },
    },);
    return await res.json();
};

export default fetcherPUT;