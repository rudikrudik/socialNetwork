import React, {useState, useEffect, createRef, useRef} from "react";
import '../config';
import NewsItem from "./NewsItem";
import axios from "axios";
import Cookies from "js-cookie";

function News() {
    const [posts, setPosts] = useState({data: [], page: 0});
    const post_limit = 10;
    const lastItem = createRef();
    const observerLoader = useRef();

    const actionInSight = (entries) => {
        if (entries[0].isIntersecting) {
            getNewPosts();
        }
    };

    const getNewPosts = () => {
        axios
            .get(`${global.config.urls.baseUrl}/post/feed/?post_limit=${post_limit}&offset=${posts.page}`, {
                mode: 'cors',
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    Cookies: `user_access_token=${Cookies.get('token')}`,
                },
            })
            .then(({ data }) => {
                if (data.length !== 0) {
                    setPosts({
                        data: [...posts.data, ...data],
                        page: posts.page + post_limit
                    });
                }
            });
        };

    //загрузка самой первой партии данных
    useEffect(() => {
        getNewPosts();
        }, []);

    //действия при изменении последнего элемента списка
    useEffect(() => {
        if (observerLoader.current) {
            observerLoader.current.disconnect();
        }
        observerLoader.current = new IntersectionObserver(actionInSight);
        if (lastItem.current) {
            observerLoader.current.observe(lastItem.current);
        }
    }, [lastItem]);

    return (
        <div className="main">
            <div>
                {posts.data.map((item, index) => {
                    //если компонент последний в списке,
                    if (index + 1 === posts.data.length) {
                        //сохраняем на него ссылку через передачу ему пропс ref
                        return <NewsItem key={parseInt(item[0])} data={item}  ref={lastItem}/>;
                    }
                    return <NewsItem key={parseInt(item[0])} data={item} />;
                })}
            </div>
        </div>
    )
}

export default News;