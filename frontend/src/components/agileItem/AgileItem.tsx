import React, { useState } from "react";
import { createPortal } from 'react-dom';

import AgileTask from "../agileTask/AgileTask";
import ModalTasks from "../modalTasksCreate/ModalTasks";

import plus from '../../icons/plus.svg';

interface Props {
    title: string
}

const AgileItem: React.FC<Props> = (props) => {
    const [open, setOpen] = useState(false);

    return (
        <div className="agileItem">
            <p className="agileItem__title">{props.title}</p>

            {Array.from(['', '']).map((item, index) => {
                return <AgileTask key={index} data={item} />
            })}
                

            <div className="agileItem__create" onClick={() => setOpen(true)}>
                <img src={plus} alt="" />
                <p>New Task</p>
            </div>

            {open && createPortal(<ModalTasks handleClick={() => setOpen(false)} />, document.body)}
        </div>
    )
}

export default AgileItem;