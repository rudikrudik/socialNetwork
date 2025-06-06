const fetch_with_args = async (url, headers, {arg}) => {
//    return await fetch(url, {
//        method: 'POST',
//       headers: {
//            'Content-Type': 'application/json',
//        },
//        body: JSON.stringify(arg),
//    }).then(res => res.json());
    const res = await fetch(url, { headers }, {arg});
    if (!res.ok) {
        const error = new Error('An error occurred while fetching the data.');
        error.info = await res.json();
        error.status = res.status;
        throw error;
    }
    return await res.json();
}

export default fetch_with_args;
