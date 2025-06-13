import Cookies from "js-cookie";

const fetcherGet = async (url) => {
    const res = await fetch(url, {
        mode: 'cors',
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            Cookies: `user_access_token=${Cookies.get('token')}`,
            }
        });

    return await res.json();
};
export default fetcherGet;