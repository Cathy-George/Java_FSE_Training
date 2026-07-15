import React from "react";

class Posts extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            posts: []
        };
    }

    loadPosts() {

        fetch("https://jsonplaceholder.typicode.com/posts")
            .then(response => response.json())
            .then(data => {
                this.setState({
                    posts: data
                });
            })
            .catch(error => {
                console.log(error);
            });

    }

    componentDidMount() {
        this.loadPosts();
    }

    componentDidCatch(error, info) {
        alert(error);
        console.log(info);
    }

    render() {

        return (

            <div className="container">

                <h1 className="title">📰 Latest Blog Posts</h1>

                {
                    this.state.posts.map(post => (

                        <div className="card" key={post.id}>

                            <div className="cardHeader">
                                <span className="badge">BLOG #{post.id}</span>
                            </div>

                            <h2>{post.title}</h2>

                            <p>{post.body}</p>

                        </div>

                    ))
                }

            </div>

        );

    }

}

export default Posts;