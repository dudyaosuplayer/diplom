import React from "react";

import plus from '../../icons/plus.svg';

interface Props {
    title: string
}

const AgileItem: React.FC<Props> = (props) => {
    return (
            <div className="agileItem">
                <p className="agileItem__title">{props.title}</p>

                {Array.from(['', '', '']).map((item, index) => {
                    return <div className="agileTask" key={index}>
                                <p className="agileTask__text-small">Category</p>
                                <p className="agileTask__text">Description Top</p>
                                <img src="" alt="" />
                            </div>
                })}
                

                <div className="agileItem__create">
                    <img src={plus} alt="" />
                    <p>New Task</p>
                </div>
            </div>
    )
}

export default AgileItem;