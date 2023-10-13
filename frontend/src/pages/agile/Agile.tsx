import React from "react";

import AgileItem from "../../components/agileItem/AgileItem";

import "../../styles/main.scss";
import "./agile.scss";

const Agile: React.FC = () => {
    return (
        <main className="agile">
            <AgileItem title="Разработка" />

            <AgileItem title="Ревью" />

            <AgileItem title="Готово" />
        </main>
    )
}

export default Agile;