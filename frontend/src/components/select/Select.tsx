import React, { useMemo } from "react";
import {Field, ErrorMessage } from 'formik';
import clsx from 'clsx';

import '../../styles/input.scss';

interface Props {
    arr: number[] | string[],
    required: boolean,
    label: string,
    name: string,
    optionText?: string,
    addEmptyOption: boolean,
    /* size?: string, */
    errors?: any,
    isSubmitting: boolean,
}

const Select: React.FC<Props> = (props) => {
    let array = props.arr;
    let classes = useMemo(() => {
        return clsx('input__field',
                    { 'input__field-red': props.errors && props.errors[props.name],
                      /* 'input__field-medium': props.size === 'medium' */});
    }, [props.isSubmitting]);

    return (
        <div className="input">
            <label htmlFor={props.name} className="input__label">
                {props.label} {props.required && <span>*</span>}
            </label>
            <Field as="select"
            name={props.name}
            className={classes}        
            id={props.name}
            >
                {props.addEmptyOption && (
                        <option value={""} className="input__option" key={""}> </option>)}
                {array.map(item => {
                    return (
                        <option value={item} className="input__option" key={item}>
                            {item.toString().toLowerCase()}{props.optionText && props.optionText}
                        </option>)
                })}
            </Field>
            <ErrorMessage
            component="div"
            name={props.name}
            className="input_error"
            />
        </div>
    )
}

export default Select;