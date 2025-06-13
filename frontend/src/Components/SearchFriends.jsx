import React, {useState} from "react";
import useSWR from "swr";
import fetcherGet from "./FetcherGET";
import useSWRMutation from "swr/mutation";
import fetcherPUT from "./FetcherPUT";

function SearchFriends() {
    const [getInputField, setInputField] = useState();

    const {
        trigger
    } = useSWRMutation([`${global.config.urls.baseUrl}/user/all`],
        ([url]) => fetcherPUT(url));


    const searchFriend = async () => {
        let result = await trigger()
        console.log(result)
    };


    return (
        <div className="search_friend">
            <input className="input-field" placeholder="Search..." onClick={searchFriend}></input>
        </div>
    )
}

export default SearchFriends;