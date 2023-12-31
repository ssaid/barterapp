import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import { Card,
  CardHeader,
  CardBody,
  CardFooter,
  Input,
  Button,
  Divider,
  Select,
  SelectItem,
  Textarea,
  Chip,
} from "@nextui-org/react";
import { Image, Post } from '../../../types/post';
import { DragAndDropFiles } from '../../posts/components/DragAndDropFiles';
import { ImageUploadPreview } from '../../posts/components/ImageUploadPreview';
import { useMemo } from 'react';
import { parseError } from '../../../utils/parseError';
import { LoadingWithBackdrop } from '../../../components/LoadingWithBackdrop';
import { useCategories } from '../../categories/hooks/useCategories';
import { useGetPost } from '../hooks/useGetPost';
import { useParams } from 'react-router-dom';
import { Category } from '../../../types/category';


const validationSchema = Yup.object({
  title: Yup.string().required('Este campo es requerido'),
  description: Yup.string().required('Este campo es requerido'),
  images: Yup.array().of(Yup.string()).min(1, 'El post debe tener al menos una foto').required('Debe agregar al menos una imagen'),
  categories: Yup.array().of(Yup.string()).min(1, 'Debe seleccionar al menos una categoria')
})

export const EditPostForm = () => {

  const { id } = useParams()

  const { categories } = useCategories();
  const { post } = useGetPost(id)

  if (categories.isLoading || post.isLoading) return <LoadingWithBackdrop />

  const initialValues: Post = {
    ...post.data,
    categories: (post.data.categories as Category[]).map(category => category.id),
  }

  return (
    <Card className="max-w-3xl w-full py-5">
      <CardHeader className='ml-3 justify-center text-lg'>Crear un post</CardHeader>
      <Divider className='my-3'/>
      <Formik
        initialValues={initialValues}
        onSubmit={() => console.log('submit')}
        validationSchema={validationSchema}
      >
        {
          formik => {

            const images = useMemo(() => {
              //@ts-ignore
              return formik.values.images.map(image => {
                if (image instanceof File) return URL.createObjectURL(image)

                return image.small_square_crop
              })
            }, [formik.values.images]);

            return (
              <Form>
                <CardBody className='flex flex-col gap-3'>
                  <Field 
                    as={Input}
                    variant="bordered"
                    name="title" 
                    type="title" 
                    color={formik.touched.title && formik.errors.title ? "danger" : ""}
                    label="Titulo" 
                    validationState={formik.touched.title && formik.errors.title ? "error" : ""}
                    errorMessage={formik.touched.title && formik.errors.title && formik.errors.title}
                  />
                  <Field 
                    as={Textarea}
                    variant="bordered"
                    name="description" 
                    type="description" 
                    color={formik.touched.description && formik.errors.description ? "danger" : ""}
                    label="Descripcion" 
                    validationState={formik.touched.description && formik.errors.description ? "error" : ""}
                    errorMessage={formik.touched.description && formik.errors.description && formik.errors.description}
                  />
                  <Field name="categories">
                    {
                      ({ field, form, meta }) =>
                        <Select
                          label="Categorias"
                          items={categories.data}
                          selectionMode="multiple"
                          placeholder="Selecciona una o mas categorias"
                          color={meta.touched && meta.error ? "danger" : "default"}
                          errorMessage={meta.touched && meta.error && meta.error}
                          value={field.value}
                          defaultSelectedKeys={post.data.categories.map(category => category.id.toString())}
                          onClose={() => form.setFieldTouched('categories', true)}
                          onChange={ e => form.setFieldValue('categories', e.target.value ? e.target.value.split(',') : []) }
                          variant='bordered'
                          classNames={{
                            label: 'py-2',
                            trigger: "min-h-unit-12 h-full py-2",
                          }}
                          renderValue={
                            items =>
                              <div className="flex flex-wrap gap-2">
                                {
                                  items.map(item => 
                                    <Chip key={item.key}>{ item.data.name }</Chip>
                                  )
                                }
                              </div>
                          }
                        >
                          {
                            category => 
                              <SelectItem key={category.id} value={category.id}>
                                {category.name}
                              </SelectItem>
                          }
                        </Select>
                    }
                  </Field>


                  <div className='flex items-center justify-center gap-3 flex-col sm:flex-row'>
                    <DragAndDropFiles
                      files={formik.values.images as File[]}
                      accept={["image/*"]}
                      onChange={files => formik.setFieldValue("images", files)}
                    />
                  </div>
                  <ErrorMessage name="images" component="div" className="text-danger text-tiny" />
                  <div className="flex flex-row gap-3 m-w-full overflow-auto p-3">
                    {
                      ( formik.values.images as Image[] ).flatMap(image => image.image.small_square_crop).map( (image: any, idx: any) => 
                        <ImageUploadPreview 
                          key={idx}
                          img={image}
                          onClick={() =>
                            //@ts-ignore
                            formik.setFieldValue('images', [...formik.values.images.filter((_, i: number) => i !== idx)]) 
                          }
                        />
                      )
                    }
                  </div>
                </CardBody>
                <CardFooter className="justify-end px-5">
                  <Button 
                    variant="solid" 
                    color="primary" 
                    type="submit" 
                    //isLoading={postMutation.isLoading || imagesMutation.isLoading}
                  >
                    Guardar cambios
                  </Button>
                </CardFooter>
                <div className='relative bottom-0 sm:h-5 h-12 -mb-5 mt-4'>
                  {/* <p className={`text-white absolute w-full bottom-0 bg-danger text-center transition duration-500 py-1 ${postMutation.isError ? '' : 'translate-y-20 '} `} > */}
                  {/*   {parseError(postMutation.error) || "Ha ocurrido un error. Vuelve a intentar mas tarde."} */}
                  {/* </p> */}
                  {/* <p className={`text-white absolute w-full bottom-0 bg-danger text-center transition duration-500 py-1 ${imagesMutation.isError ? '' : 'translate-y-20'} `} > */}
                  {/*   {parseError(imagesMutation.error) || "Ha ocurrido un error. Vuelve a intentar mas tarde."} */}
                  {/* </p> */}
                </div>
              </Form>
            )
          }
        }
      </Formik>
    </Card>
  )


}
