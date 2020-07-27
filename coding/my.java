public static void main(String[] args) throws IOException {
       /**
        * 请求参数内容加密
        * 1.生成body内容
        * 2.得到加密的sign串(sign=md5(appid+body+appkey))
        * 3.组合请求格式串
        * 4.请求串转为json string
        * 5.json string的请求串增加base64 decode
        */
 
       // 生成body内容
       JSONObject body = new JSONObject();
       body.put("sql", "select * from ods_xm_fact_daily_mfg_process limit 20");
       body.put("userId","xxx");
 
       // 得到加密的sign串(sign=md5(appid+body+appkey))
       String appId = "xxxx";
       String appKey = "xxxxxxx";
       String sign = DigestUtils.md5Hex(appId + JSON.toJSONString(body) + appKey);
 
       // 请求内容
       JSONObject header = new JSONObject();
       header.put("appid", appId);
       header.put("sign", sign);
       header.put("method", "/v1/task/service-submit-async");
       JSONObject request = new JSONObject();
       request.put("header", header);
       request.put("body", JSON.toJSONString(body));
 
       // 请求内容base64 decode
       String data = Base64.getEncoder().encodeToString(JSON.toJSONString(request).getBytes());
 
       // 发送请求
       List<BasicNameValuePair> params = new ArrayList<>();
       params.add(new BasicNameValuePair("data", data));
       CloseableHttpClient client = HttpClients.createDefault();
       HttpPost httpPost = new HttpPost("http://xdata.be.xiaomi.com/executor-api/v1/task/service-submit-async");
       httpPost.setEntity(new UrlEncodedFormEntity(params));
       CloseableHttpResponse response = client.execute(httpPost);
       HttpEntity entity = response.getEntity();
 
       String content = EntityUtils.toString(entity);
       // 结果
       System.out.println(content);
       client.close();
   }