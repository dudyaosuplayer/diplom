import React from "react";

import "../../styles/main.scss";
import "./home.scss";

const Home: React.FC = () => {
    return (
        <main className="home">
            <h2>Мои проекты:</h2>
            <ol>
                <li><a href="#">Неофлекс</a></li>
                <li><a href="#">Неоджира</a></li>
            </ol>         
        </main>
    )
}

export default Home;