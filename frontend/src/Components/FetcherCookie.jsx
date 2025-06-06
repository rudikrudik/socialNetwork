const fetcher_cookie = async (url, headers) => {
    const res = await fetch(url, { headers });
    if (!res.ok) {
        const error = new Error('An error occurred while fetching the data.');
        error.info = await res.json();
        error.status = res.status;
        throw error;
    }
    return await res.json();
};

export default fetcher_cookie;