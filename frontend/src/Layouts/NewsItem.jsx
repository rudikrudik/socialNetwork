import React, { forwardRef } from 'react'
import profile_img from "../images/profile/6.jpg"
import useSWR from "swr";
import fetcherGet from "../Components/FetcherGET";


const NewsItem = forwardRef((props, ref) => {
    const date = new Date(Date.parse(props.data[2].toString()));
    const formattedDate = new Intl.DateTimeFormat('en-US', {
        hour12: false,
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
    }).format(date);

    const {
        data,
        isLoading,
        error
    } = useSWR([`${global.config.urls.baseUrl}/user/get/?id_user=${props.data[1]}`],
        ([url]) => fetcherGet(url));


    if (isLoading) return <div>is Loading</div>;
    if (error) return <div>Error</div>;

    return ( <div className="post" ref={ref}>
            <div className="post_author_menu_wrapper">
                <div className="post_author">
                    <img alt="profile logo" src={profile_img}/>
                    <p>{data.first_name} {data.last_name}</p>
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
                    <button className="post_menu_button_delete">Dislike</button>
                    <button className="post_menu_button_edit">Like</button>
                </div>
            </div>
        </div> )
    });

export default NewsItem;