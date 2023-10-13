import React, { useState } from "react";

import { Formik, Form } from 'formik';
import * as Yup from "yup";
import Button from "../button/Button";
import Input from "../input/Input";
import './modal.scss';


const validationSchema = Yup.object().shape({
    name: Yup.string().required("Put the name"),
    description: Yup.string().required("Put the description"),
    money: Yup.string().required("What about money"),
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
                        money: "",
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

                            <Input type='text' name='money' label='Сумма проекта' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='10000 руб.' required={true} 
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