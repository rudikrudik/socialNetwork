import React, {useState} from "react";
import useSWRMutation from "swr/mutation";
import updatePost from "../Components/UpdatePost";
import {useNavigate} from "react-router-dom";


function CreatePost () {
    const navigate = useNavigate();
    const [getInputContent, setInputContent] = useState("")

    const handleChange = (e) => {
        setInputContent(e.target.value);
    };

    const {
        trigger
    } = useSWRMutation(`${global.config.urls.baseUrl}/post/create`, updatePost)

    const handlerClick = async () => {
        let result = await trigger(getInputContent)
        if (result[1] === "ok") {
            console.log("Post create:")
            window.location.reload();
        }
        else {
            console.log(result)
        }
    }

    return (
        <div className="create_post_menu_wrapper">
            <div className="create_post_menu">
                <input onInput={setInputContent} onChange={handleChange} ></input>
                <button className="post_menu_button_edit" onClick={handlerClick}>Create</button>
            </div>
        </div>
    )
}

export default CreatePost;