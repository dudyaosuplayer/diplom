import React, { useState } from "react";
import { createPortal } from 'react-dom';

import Button from "../../components/button/Button";
import ModalProject from "../../components/modalProject/ModalProject";
import Table from "../../components/table/Table";

import "../../styles/main.scss";
import "./projects.scss";


const dataTitles = ['Название', 'Описание', 'Участники', 'Начало', 'Завершение', 'Статус'];
const dataInfo = [
    {
        name: 'Неофлекс',
        description: 'aaaa', 
        participants: 'ann',
        begin: '1',
        end: '4',
        status: 'work'
    },
    {
        name: 'Неоджира',
        description: 'bbb', 
        participants: 'bob',
        begin: '5',
        end: '9',
        status: 'begin'
    },
    {
        name: 'Something',
        description: 'ccc', 
        participants: 'cat',
        begin: '4',
        end: '9',
        status: 'work'
    }
];

const sorting = ['name', 'description', 'participants', 'begin', 'end', 'status'];

const Projects: React.FC = () => {
    const [open, setOpen] = useState(false);

    return (
        <main className="projects">
            <div className="projects__buttons" onClick={() => setOpen(true)}>
                <Button text="Создать проект" />
            </div>

            <Table titles={dataTitles} data={dataInfo} sorting={sorting} />

            {open && createPortal(<ModalProject handleClick={() => setOpen(false)} />, document.body)}
        </main>
    )
}

export default Projects;