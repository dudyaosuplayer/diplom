import React from "react";
import clsx from 'clsx';

import './button.scss';

interface Props {
    type?: "button" | "submit",
    text: string,
    color?: string,
} 

const Button: React.FC<Props> = (props) => {
    let classes = clsx('button',
                    { 'button__pink': props.color === 'pink' });
    
    return (
        <button className={classes} type={props.type}>
            <span>{props.text}</span>
        </button>
    )
}

export default Button;