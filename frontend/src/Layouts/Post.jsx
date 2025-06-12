import React from 'react'
import profile_img from "../images/profile/6.jpg"
import EditPost from "../Components/EditPost";
import DeletePost from "../Components/DeletePost";


function Post(props) {
    const date = new Date(Date.parse(props.data[2].toString()));
    const formattedDate = new Intl.DateTimeFormat('en-US', {
        hour12: false,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);

    return (
        <div className="post">
            <div className="post_author_menu_wrapper">
                <div className="post_author">
                    <img alt="profile logo" src={profile_img}/>
                    <p>{props.user_prop.first_name} {props.user_prop.last_name}</p>
                </div>
                <div className="post_post_date">
                    <p>{formattedDate}</p>
                </div>
            </div>
            <div className="post_content_menu">
                <p>{props.data[3]}</p>
            </div>
            <div className="post_edit_menu_wrapper">
                <div className="post_edit_menu">
                    <EditPost id_post={props.data[0]} content={props.data[3]}/>
                    <DeletePost id_post={props.data[0]}/>
                </div>
            </div>
        </div>
    )
}

export default Post