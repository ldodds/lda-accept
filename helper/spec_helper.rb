require 'rubygems'
require 'spec'
require 'rest_client'
require 'json'
require 'siren'

def server_get(path, opts = {})
  RestClient.get "#{ENV['server']}/#{path}", opts
end

def query(response, query)
  json = JSON.parse(response.body)
  return Siren.query(query, json)
end
