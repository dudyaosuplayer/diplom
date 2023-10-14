import React, { useState } from "react";
import { createPortal } from 'react-dom';

import ModalTaskInfo from "../modalTasksInfo/ModalTasksInfo";

import image from '../../images/picture.png'

interface Props {
    data?: any
}

const AgileTask: React.FC<Props> = (props) => {
    const [open, setOpen] = useState(false);

    return (
        <div className="agileTask">
            <p className="agileTask__text-small" onClick={() => setOpen(true)}>
                Category
            </p>
            <p className="agileTask__text" onClick={() => setOpen(true)}>
                Description Top
            </p>
            <div className="agileTask__image" onClick={() => setOpen(true)}>
                <img src={image} alt="" />
            </div>

            {open && createPortal(<ModalTaskInfo data={props.data} handleClick={() => setOpen(false)} />, document.body)}
        </div>
            
    )
}

export default AgileTask;