import React, { useState } from "react";
import { createPortal } from 'react-dom';
import { Link, useLocation } from "react-router-dom";

import ModalProjectInfo from "../modalProjectInfo/ModalProject";
import ModalTaskInfo from "../modalTasksInfo/ModalTasksInfo";


interface Props {
    data: object,
} 


const TableRow: React.FC<Props> = (props) => {
    let location = useLocation();

    let modal = <ModalProjectInfo data={props.data} handleClick={() => setOpen(false)} />

    if (location.pathname === '/tasks') {
        modal = <ModalTaskInfo data={props.data} handleClick={() => setOpen(false)} />
    }

    const [open, setOpen] = useState(false);

    return (
        <>
        <tr className="table__row" >
            {
                Object.values(props.data).map((el, index) => {
                    if (location.pathname === '/tasks') {
                        return <td key={index} >
                                    {String(el)}
                                </td>
                    } else {
                        return <td key={index} >
                                    <Link to="/tasks" >
                                        {String(el)}
                                    </Link>
                                </td>
                    }
                })
            }
            <td className="table__edit" onClick={() => setOpen(true)}>Редактировать</td>
        </tr>
        
        {open && createPortal(modal, document.body)}
        </>
    )
}

export default TableRow;