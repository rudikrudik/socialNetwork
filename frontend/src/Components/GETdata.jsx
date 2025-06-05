function sendGetRequest(url, { arg }) {
    return fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(arg),
    }).then(res => res.json());
}

export default sendGetRequest;