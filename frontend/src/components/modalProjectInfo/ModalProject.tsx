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
    participants: Yup.string().required("Put participants"),
    start: Yup.string().required("Put the begin"),
    finish: Yup.string().required("Put the end"),
    money: Yup.string().matches(/^\d+$/, "Only numbers").trim()
        .required("The series must be 4 digits"),
    status: Yup.string().required("Put the status"),
});

interface Props {
    handleClick: Function,
    data: any,
}

const ModalProjectInfo: React.FC<Props> = (props) => {
    function closeModal() {
        props.handleClick();
    }
    
    const [data, setData] = useState(props.data);

    return (
        <div className="modal">
            <div className="modal__message">
                <div className="modal__title">
                    <p>Редактирование Проекта</p>
                    <div onClick={closeModal}>
                        x
                    </div>
                </div>

                <Formik
                    initialValues={{ 
                        name: data.name,
                        description: data.description,
                        participants: data.participants,
                        start: data.begin,
                        finish: data.end,
                        money: "",
                        status: data.status
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

                            <Input type='text' name='participants' label='Участники' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Вася' required={true} 
                                />

                            <InputDate type='date' label='Дата начала проекта' name='start'
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} placeholder='Выберите дату' />

                            <InputDate type='date' label='Дата завершения проекта' name='finish'
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    required={true} placeholder='Выберите дату' />

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
                                <Button type="submit" text='Сохранить изменения' />
                            </div> 
                        </Form>
                    )}
                </Formik>        
                
            </div>
        </div>
    )
}

export default ModalProjectInfo;