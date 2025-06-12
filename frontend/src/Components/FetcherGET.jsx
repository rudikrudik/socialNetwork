import Cookies from "js-cookie";

const fetcherGet = async (url) => {
    const res = await fetch(url, {
        mode: "cors",
        method: 'GET',
        credentials: 'include',
        headers: {
            'Access-Control-Allow-Origin': 'http://api.vsadmin.ru/',
            'Content-Type': 'application/json'
        },
    },);

    return await res.json();
};

export default fetcherGet;

//            Cookies: `user_access_token=${Cookies.get('token')}`,