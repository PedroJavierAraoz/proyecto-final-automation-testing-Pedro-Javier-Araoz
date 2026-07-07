from pages.post_api_page import PostApi
from utils.logger import logger
import pytest_check as check


api= PostApi()

def test_get_one_post ():

    logger.info("obteniendo un post")
    response=api.get_one_post(1)

    expected_code=200
    expected_id= 2

    #capturare los  errores  del check de  dos  formas  distintas  para  poder  escribir  el log del fallo

    # primeros registrando  el  valor que devuelve  check
    paso_status=check.equal(
        response.status_code, expected_code,"Status incorrecto"
    )
    if not paso_status:
        logger.error(f"El test falló, status {response.status_code}")

    body=response.json()

    #ahora, manejaremos  el  log en caso de error  captiurandpo la excecion  la  lanza  chek cuandop el test  falla
    try:
        check.equal(
            body["id"], expected_id, "No coincide el id del post"
        )
        #voy a  forzar  a que lance  la excepcion,  deberia  lanzarla   solo con  el fallo del check, pero no lo esta haciendo
        if check.any_failures():
            raise AssertionError("No coincide  el id del post en el test")
        
    except AssertionError as e:
        logger.error(f" El test falló por : {e}")



def test_get_posts():

    logger.info("obteniendo todos los posts")
    response=api.get_posts()

    expected_code=200
   
    # primeros registrando  el  valor que devuelve  check
    paso_status=check.equal(
        response.status_code, expected_code,"Status incorrecto"
    )
    if not paso_status:
        logger.error(f"El test falló, status {response.status_code}")

    posts=response.json()

 
    paso_len= check.is_true(
            len(posts)>0, "No  se  recibieron  datos"
        )
        #voy a  forzar  a que lance  la excepcion,  deberia  lanzarla   solo con  el fallo del check, pero no lo esta haciendo
    if not paso_len:
        logger.error(f"El test falló, no hay datos {len(posts)}")


def test_create_post(post_data):
    expected_code=200

    logger.info("Creo un nuevo post")

    response = api.create_post(
        post_data['title'], 
        post_data['body'], 
        post_data['userId']
        )
    pass_create= check.equal(expected_code, response.status_code, "status incorrecto")
    if not  pass_create:
        logger.error(f"El test falló, status {response.status_code}")

    

  


