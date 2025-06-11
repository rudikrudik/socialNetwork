import Cookies from "js-cookie";

const fetcherPUT = async (url) => {
    const res = await fetch(url, {
        mode: "cors",
        method: 'PUT',
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:3000',
            Cookies: `user_access_token=${Cookies.get('user_access_token')}`,
            'Content-Type': 'application/json'
        },
    },);

    return await res.json();
};

export default fetcherPUT;