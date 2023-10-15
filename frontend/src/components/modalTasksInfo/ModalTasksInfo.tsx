import React, { useState } from "react";

import { Formik, Form } from 'formik';
import * as Yup from "yup";
import Button from "../button/Button";
import Input from "../input/Input";
import Select from "../select/Select";

import './modal.scss';


const validationSchema = Yup.object().shape({
    name: Yup.string().required("Put the name"),
    description: Yup.string().required("Put the description"),
    deadline: Yup.date().required(`Incorrect date`),
    executor: Yup.string().required("Put the executor"),
    priority: Yup.string().required("Put the priority"),
    status: Yup.string().required("Put the status"),
});

interface Props {
    handleClick: Function,
    data: any,
}

const ModalTaskInfo: React.FC<Props> = (props) => {
    function closeModal() {
        props.handleClick();
    }
    
    const [data, setData] = useState(props.data);

    return (
        <div className="modal">
            <div className="modal__message">
                <div className="modal__title">
                    <p>Редактирование Задачи</p>
                    <div onClick={closeModal}>
                        x
                    </div>
                </div>

                <Formik
                    initialValues={{ 
                        name: data.name,
                        description: data.description,
                        deadline: data.deadline,
                        executor: data.executor,
                        priority: data.priority,
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
                                    placeholder='Эта задача ...' required={true} 
                                />

                            

                            <Input type='text' name='deadline' label='Дедлайн' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='12' required={true} 
                                />
                            
                            <Input type='text' name='executor' label='Исполнитель' 
                                    values={values} errors={errors} isSubmitting={isSubmitting}
                                    placeholder='Вася' required={true} 
                                />
                            
                            <Select name='priority' label="Приоритет задачи" required={true}
                                    arr={["высокий", "средний", "низкий"]} 
                                    addEmptyOption={true} 
                                    errors={errors} isSubmitting={isSubmitting}
                                />

                            <Select name='status' label="Статус задачи" required={true}
                                    arr={["в работе", "завершена", "на проверке"]} 
                                    addEmptyOption={true} 
                                    errors={errors} isSubmitting={isSubmitting}
                                />    
                             
                            <div className="form__buttons">
                                <div>
                                    <p>Задача создана {data.created}</p>
                                </div>
                                <Button type="submit" text='Сохранить изменения' />
                            </div> 
                        </Form>
                    )}
                </Formik>        
            </div>
        </div>
    )
}

export default ModalTaskInfo;