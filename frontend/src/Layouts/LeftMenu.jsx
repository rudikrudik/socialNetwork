import React from "react";
import profile from "../images/left_menu/profile_small.png"
import friends from "../images/left_menu/friends_small.png"
import posts from "../images/left_menu/posts_small.png"
import video from "../images/left_menu/video_small.png"
import music from "../images/left_menu/music_small.png"
import photo from "../images/left_menu/photo_small.png"
import message from "../images/left_menu/message_small.png"
import {Link} from "react-router-dom";
let size = "12%"


function LeftMenu () {
    return (
        <div className="left_menu">
            <div className="left_menu_block">
                <Link to="/profile"><p><img width={size} alt="Profile Logo" src={profile}/>
                    Profile</p></Link>
                <p><Link to="/friends"><img width={size} alt="Profile Logo" src={friends}/>
                    Friends</Link></p>
                <p><img width={size} alt="Profile Logo" src={message}/>
                    Messages</p>
                <p><Link to="/news"><img width={size} alt="Profile Logo" src={posts}/>
                    News</Link></p>
                <p><img width={size} alt="Profile Logo" src={music}/>
                    Music</p>
                <p><img width={size} alt="Profile Logo" src={video}/>
                    Videos</p>
                <p><img width={size} alt="Profile Logo" src={photo}/>
                    Photo</p>
            </div>
        </div>
    )
}

export default LeftMenu;