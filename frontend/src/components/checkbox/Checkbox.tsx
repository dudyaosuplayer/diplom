import React from "react";
import {Field, ErrorMessage } from 'formik';

import "checkbox.scss";


interface Props {
    name: string,
    text: string,
} 

const Checkbox: React.FC<Props> = (props) => {
    return (
        <>
            <Field type="checkbox" name={props.name} id={props.name} className="checkbox" />
            <label htmlFor="agree" className="checkbox__label">{props.text}</label>
            <ErrorMessage
            component="div"
            name={props.name}
            className="input_error"
            />
        </>
    )
}

export default Checkbox;