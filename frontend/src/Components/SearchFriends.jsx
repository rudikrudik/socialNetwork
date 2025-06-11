import React, {useState} from "react";

function SearchFriends() {
    const [getInputField, setInputField] = useState();

    return (
        <div className="search_friend">
            <input className="input-field" placeholder="Search..."></input>
        </div>
    )
}

export default SearchFriends;