# Rules OWASP associated with acl
variable "rules" {
  type = list(any)
  default = [
    # {
    #   name                                     = "SQLiRuleSet"
    #   priority                                 = 20
    #   managed_rule_group_statement_name        = "AWSManagedRulesSQLiRuleSet"
    #   managed_rule_group_statement_vendor_name = "AWS"
    #   metric_name                              = "SQLiRuleSet-rule-metric"
    #   excluded_rules                           = []
    # },
    {
      name                                     = "WordPress_application"
      priority                                 = 25
      managed_rule_group_statement_name        = "AWSManagedRulesWordPressRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "WordPress_application-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "AWS_IP_Reputation_List"
      priority                                 = 30
      managed_rule_group_statement_name        = "AWSManagedRulesAmazonIpReputationList"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "AWS_IP_Reputation-rule-metric"
      excluded_rules                           = []
    },
    # {
    #   name                                     = "Admin_Protection"
    #   priority                                 = 35
    #   managed_rule_group_statement_name        = "AWSManagedRulesAdminProtectionRuleSet"
    #   managed_rule_group_statement_vendor_name = "AWS"
    #   metric_name                              = "Admin_Protection-rule-metric"
    #   excluded_rules                           = []
    # },
    {
      name                                     = "PHP_application"
      priority                                 = 40
      managed_rule_group_statement_name        = "AWSManagedRulesPHPRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "PHP_application-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "Posix_Operating_System"
      priority                                 = 45
      managed_rule_group_statement_name        = "AWSManagedRulesUnixRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "Posix_Operating_System-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "LinuxRuleSet"
      priority                                 = 50
      managed_rule_group_statement_name        = "AWSManagedRulesLinuxRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "LinuxRuleSet-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "Known_Bad_Inputs"
      priority                                 = 55
      managed_rule_group_statement_name        = "AWSManagedRulesKnownBadInputsRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "Known_Bad_Inputs-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "WindowsRuleSet"
      priority                                 = 60
      managed_rule_group_statement_name        = "AWSManagedRulesKnownBadInputsRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "WindowsRuleSet-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "Anonymous_IP_List"
      priority                                 = 65
      managed_rule_group_statement_name        = "AWSManagedRulesAnonymousIpList"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "Anonymous_IP_List-rule-metric"
      excluded_rules                           = []
    },
    {
      name                                     = "RulesBotControlRuleSet"
      priority                                 = 70
      managed_rule_group_statement_name        = "AWSManagedRulesBotControlRuleSet"
      managed_rule_group_statement_vendor_name = "AWS"
      metric_name                              = "BotControl-rule-metric"
      excluded_rules                           = []
    }
  ]
}

*


#############


resource "aws_wafv2_web_acl" "web_acl" {
  for_each    = toset(var.scope)
  name        = each.key
  scope       = each.key
  description = "ACL WAF ${each.key}"

  default_action {
    allow {}
  }
  rule {
    name     = var.waf["rule_country"]
    priority = 15
    override_action {
      none {}
    }
    statement {
      rule_group_reference_statement {
        arn = aws_wafv2_rule_group.rule_group[each.key].arn
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "metric-geolocation"
      sampled_requests_enabled   = true
    }
  }

  tags = {
    Name        = "web-acl-${each.key}"
    Environment = terraform.workspace
    terraform   = true
  }

  visibility_config {
    cloudwatch_metrics_enabled = true
    metric_name                = "metric-2"
    sampled_requests_enabled   = true
  }

  rule {
    name     = "Rate-Limit"
    priority = 75

    action {
      count {}
    }

    statement {
      rate_based_statement {
        limit              = 1000
        aggregate_key_type = "IP"

        scope_down_statement {
          geo_match_statement {
            country_codes = var.country-ip
          }
        }
      }
    }

    visibility_config {
      cloudwatch_metrics_enabled = true
      metric_name                = "Rate-Limit"
      sampled_requests_enabled   = true
    }
  }


  dynamic "rule" {
    for_each = toset(var.rules)

    content {
      name     = rule.value.name
      priority = rule.value.priority
      override_action {
        none {}
      }

      statement {
        managed_rule_group_statement {
          name        = rule.value.managed_rule_group_statement_name
          vendor_name = rule.value.managed_rule_group_statement_vendor_name
        }
      }

      visibility_config {
        cloudwatch_metrics_enabled = true
        metric_name                = rule.value.metric_name
        sampled_requests_enabled   = true
      }
    }
  }
}

resource "aws_wafv2_web_acl_association" "main" {
  count        = var.associate_alb
  resource_arn = var.alb_arn
  web_acl_arn  = aws_wafv2_web_acl.web_acl["REGIONAL"].arn
}



