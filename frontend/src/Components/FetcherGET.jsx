import Cookies from "js-cookie";

const fetcherGet = async (url) => {
    const res = await fetch(url, {
        mode: 'cors',
        method: 'GET',
        credentials: 'include',
        headers: {
            'Access-Control-Allow-Origin': 'http://192.168.0.3:3000',
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`
            }
        });

    return await res.json();
};
export default fetcherGet;

//            Cookies: `user_access_token=${Cookies.get('token')}`,