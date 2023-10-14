import React, { useState } from "react";
import { createPortal } from 'react-dom';

import ModalProjectInfo from "../../components/modalProjectInfo/ModalProject";
import ModalTaskInfo from "../../components/modalTasksInfo/ModalTasksInfo";

import "../../styles/main.scss";
import "./home.scss";

const Home: React.FC = () => {
    const [openProject, setOpenProject] = useState(false);
    const [openTask, setOpenTask] = useState(false);

    const [data, setData] = useState({})

    function openModal(id:string, mode:string) {
        setData({});
        if (mode === 'project') {
            setOpenProject(true);
        } else {
            setOpenTask(true);
        } 
    }

    return (
        <main className="home">
            <h2>Мои проекты:</h2>
            <ol>
                <li onClick={() => openModal('test', 'project')}>Неофлекс</li>
                <li onClick={() => openModal('test', 'project')}>Неоджира</li>
            </ol>   
            <h2>Мои задачи:</h2>
            <ol>
                <li onClick={() => openModal('test', 'task')}>Задача 1</li>
                <li onClick={() => openModal('test', 'task')}>Задача 2</li>
            </ol>  

            {openProject && createPortal(<ModalProjectInfo data={data} 
                    handleClick={() => setOpenProject(false)} />, document.body)}

            {openTask && createPortal(<ModalTaskInfo data={data} 
                    handleClick={() => setOpenTask(false)} />, document.body)}
        </main>
    )
}

export default Home;