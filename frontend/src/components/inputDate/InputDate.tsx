import React, { useMemo } from "react";
import {Field, ErrorMessage } from 'formik';
import clsx from 'clsx';

import '../styles/input.scss';

interface Props {
    label: string,
    required: boolean,
    placeholder: string,
    name: string,
    type: "date",
    errors: any,
    values: any,
    isSubmitting: boolean,
    size?: string,
}

const InputDate: React.FC<Props> = (props) => {
    let classes = useMemo(() => {
        return clsx('input__field',
                    { 'input__field-green': props.values[props.name]!== '' , 
                      'input__field-red': props.errors[props.name],
                      'input__field-large': props.size === 'large'  });
    }, [props.isSubmitting]);
    
    return (
        <div className="input">
            <label htmlFor={props.name} className="input__label">
                {props.label} {props.required && <span>*</span>}
            </label>
            <Field
            name={props.name}
            className={classes}
            placeholder={props.placeholder}
            id={props.name}
           /*  required={props.required} */
            onFocus={(e: React.FocusEvent<HTMLInputElement>) => (e.target.type = "date")}
            onBlur={(e: React.FocusEvent<HTMLInputElement>) => (e.target.type = "text")}
            />
            <ErrorMessage
            component="div"
            name={props.name}
            className="input_error"
            />
        </div>
    )
}

export default InputDate;