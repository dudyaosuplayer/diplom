import React, { useState } from "react";
import { createPortal } from 'react-dom';

import Button from "../../components/button/Button";
import ModalTasks from "../../components/modalTasks/ModalTasks";
import Table from "../../components/table/Table";

import "../../styles/main.scss";
import "./tasks.scss";

const dataTitles = ['Название', 'Создан', 'Дедлайн', 'Исполнитель', 'Приоритет', 'Статус'];
const dataInfo = [
    {
        name: 'Неофлекс',
        created: '11', 
        deadline: '22',
        executor: 'tom',
        priority: 'высокий',
        status: 'work'
    },
    {
        name: 'Неоджира',
        created: '22', 
        deadline: '30',
        executor: 'den',
        priority: 'низкии',
        status: 'done'
    },
    {
        name: 'Something',
        created: '12', 
        deadline: '25',
        executor: 'wally',
        priority: 'средний',
        status: 'work'
    }
];

const sorting = ['name', 'created', 'deadline', 'executor', 'priority', 'status'];

const Tasks: React.FC = () => {
    const [open, setOpen] = useState(false);

    return (
        <main className="tasks">
            <div className="tasks__buttons" onClick={() => setOpen(true)}>
                <Button text="Создать задачу" />
            </div>

            <Table titles={dataTitles} data={dataInfo} sorting={sorting} />
                    
            {open && createPortal(<ModalTasks handleClick={() => setOpen(false)} />, document.body)}
        </main>
    )
}

export default Tasks;