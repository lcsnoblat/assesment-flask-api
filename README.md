# Service Quiz



***Modelo de requisição***
----

* URL

  https://log-analytics-api-br.azurewebsites.net

* DESCRIPTION

    Endpoint responsável por receber o nome do grupo de serviço e seu serviço especifico e informar se possui questões obrigatórias ou não.

    OBS: Caso possua questões obrigatórias também será retornado as perguntas no corpo da requisição.

* Endpoint
  
    `/services-questions`

* Method:

    `GET`

*  Headers

    Content-Type:  `application/json`
    
    token: `0544b53c-801c-45cd-91a8-3cd567514e2e`

*  URL Params

    "service": `string`

    "group_service": `string`

* Request Body

    
    Não é necessário



* Success Response:
  

  * Code: 200 <br>
    Content: `
    
        
    {
        "success": true
        "service": instalation,
        "has_questions" true,
        "questions": [{
            "id": 1,
             "question": "A visita foi um sucesso?"
        },
        {
            "id": 2,
            "question": "Quais maquinas o cliente possui no balcão?"
        }]
    }



----
***Modelo de requisição***
----

* URL

  https://log-analytics-api-br.azurewebsites.net

* DESCRIPTION

    Endpoint responsável por receber respostas à questões previamente enviadas.
    
* Endpoint
  
    `/service-answers `

* Method:

    `POST`

*  Headers

    Content-Type:  `application/json`
    
    token: `0544b53c-801c-45cd-91a8-3cd567514e2e`

*  URL Params

    `Não é necessário.`

* Request Body

    
    {
        "group_service": instalation
        "service": instalation,
        "questions": [{
            "id": 1,
             "question": "A visita foi um sucesso?"
             "answer": "Sim!"
        },
        {
            "id": 2,
            "question": "Cliente ativou Collact?"
            "answer": "Não!"
        }]
    }



* Success Response:
  

  * Code: 200 <br>
    Content: 
    
        
    {
        "success": true,
        "message": Perguntas salvas com sucesso!
    }
