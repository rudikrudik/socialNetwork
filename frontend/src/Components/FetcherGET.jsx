import Cookies from "js-cookie";

const fetcherGet = async (url) => {
    const res = await fetch(url, {
        method: 'GET',
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`,
            }
        });

    return await res.json();
};
export default fetcherGet;

//            Cookies: `user_access_token=${Cookies.get('token')}`,