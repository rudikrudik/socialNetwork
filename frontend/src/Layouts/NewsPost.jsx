import React from 'react'
import profile_img from "../images/profile/6.jpg"


function NewsPost(props) {
    const date = new Date(Date.parse(props.data[2].toString()));
    const formattedDate = new Intl.DateTimeFormat('en-US', {
        hour12: false,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);

    console.log("NewsPost", props.data)

    return (
        <div className="post">
            <div className="post_author_menu_wrapper">
                <div className="post_author">
                    <img alt="profile logo" src={profile_img}/>
                    <p>First Name Last Name</p>
                </div>
                <div className="post_post_date">
                    <p>{formattedDate}</p>
                </div>
            </div>
            <div className="post_content_menu">
                <p>{props.data[3]}</p>
            </div>
            <div className="post_edit_menu_wrapper">
            </div>
        </div>
    )
}

export default NewsPost