import React, { useState } from "react";

import { Formik, Form } from 'formik';
import * as Yup from "yup";
import Button from "../button/Button";
import Input from "../input/Input";
import Select from "../select/Select";
import InputDate from "../inputDate/InputDate";

import './modal.scss';


const validationSchema = Yup.object().shape({
    name: Yup.string().required("Put the name"),
    description: Yup.string().required("Put the description"),
    start: Yup.date().required(`Incorrect date`),
    finish: Yup.date().required(`Incorrect date`),
    purpose: Yup.string().required("Put the purpose"),
    money: Yup.string().matches(/^\d+$/, "Only numbers").trim()
        .required("The series must be 4 digits"),
    status: Yup.string().required("Select one of the options"),
});

interface Props {
    handleClick: Function
}

const ModalProject: React.FC<Props> = (props) => {
    function closeModal() {
        props.handleClick();
    }

    return (
        <div className="modal">
            <div className="modal__message">
                <div className="modal__title">
                    <p>Создание Проекта</p>
                    <div onClick={closeModal}>
                        x
                    </div>
                </div>

                <Formik
                    initialValues={{ 
                        name: "",
                        description: "",
                        start: '',
                        finish: '',
                        purpose: '',
                        money: "",
                        status: '',
                    }}
                    validateOnChange={false}
                    validateOnBlur={true}
                    onSubmit={(val) => {
                        console.log('submit');
                        closeModal();
                    }}
                    validationSchema={validationSchema}
                >
                    {({values, errors, isSubmitting}) => (
                        <Form className="form" >
                            <Input type='text' name='name' label='Название проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Название' required={true} 
                                />

                            <Input type='text' name='description' label='Описание проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Этот проект ...' required={true} 
                                />

                            <InputDate type='date' label='Дата начала проекта' name='start'
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} placeholder='Выберите дату' />

                            <InputDate type='date' label='Дата завершения проекта' name='finish'
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} placeholder='Выберите дату' />

                            <Input type='text' name='purpose' label='Цель проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Цель проекта ...' required={true} 
                                />

                            <Input type='text' name='money' label='Сумма проекта' 
                                placeholder='10000' required={true} errors={errors} 
                                isSubmitting={isSubmitting} values={values}
                                />

                            <Select name='status' label="Статус проекта" required={true}
                                    arr={["активный", "завершен"]} 
                                    addEmptyOption={true} 
                                    errors={errors} isSubmitting={isSubmitting}
                                />
                                
                            <div className="form__buttons">
                                <Button type="submit" text='Создать' />
                            </div> 
                        </Form>
                    )}
                </Formik>        
                
            </div>
        </div>
    )
}

export default ModalProject;